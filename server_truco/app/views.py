# -*- coding: utf-8 -*-
from django.template.context import RequestContext
from django.http import HttpResponse, HttpResponseRedirect,\
	HttpResponseForbidden, HttpResponseServerError, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404, render_to_response,\
	redirect
from django.core import serializers
from app.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from app.forms import StoreForm
from django.utils.simplejson import dumps
from django.utils.translation import ugettext as _
from django.template.defaulttags import ifequal
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_view(request):
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		try:
			user = authenticate(username=username, password=password)
		except :
			user = None
		if user is not None:
			if user.is_active:
				if 'remember_me' in request.POST:
					request.session.set_expiry(1209600)
				login(request, user)
				if request.POST.has_key('mobile') and request.POST['mobile'] == 'True':
					if 'next' in request.POST:
						return HttpResponseRedirect(request.POST['next'])
					else :
						result = {'result':'Ok'}
						response_json = json.dumps(result)
						response = HttpResponse(response_json, mimetype="application/json")
						response['Cache-Control'] = 'no-cache' 
						return response
				else:
					return redirect('home')
				# Redirect to a success page.
			else:
				# Return a 'disabled account' error message
				if request.POST.has_key('mobile') and request.POST['mobile'] == 'True':
					result = {'result':'Fail','message':'Cuenta desactivada'}
					response_json = json.dumps(result)
					response = HttpResponse(response_json, mimetype="application/json")
					response['Cache-Control'] = 'no-cache' 
					return response	
				else:			
					messages.add_message(request, messages.ERROR, _(u'Cuenta' +
				+'desactivada.'))
		else:
		# Return an 'invalid login' error message.
			if request.POST.has_key('mobile') and request.POST['mobile'] == 'True':
				result = {'result':'Fail','message':'Usuario o clave incorrecto'}
				response_json = json.dumps(result)
				response = HttpResponse(response_json, mimetype="application/json")
				response['Cache-Control'] = 'no-cache' 
				return response
			else:
				messages.add_message(request, messages.ERROR,
								 _(u'El Usuario o Password no es válido.'))
			return render_to_response('registration/login.html',
							context_instance=RequestContext(request))
	return render_to_response('registration/login.html',
							context_instance=RequestContext(request))		


def home(request):
	data = {}
	places = []
	if request.user.is_authenticated():
		template = 'dashboard.html'
	else:
		template = 'home.html'
		places = Place.objects.select_related('store').all()
		data = {
			"count_users" : Consumer.objects.count(),
			"places" : Place.objects.all()
			}
	return render_to_response(template, data , context_instance=RequestContext(request))


@login_required
def list_stores(request):
	"""
	List all store from a customer User
	"""	
	manager = Manager.objects.get(user=request.user)
	stores = manager.store_set.all()
	for s in stores:
		places = Place.objects.filter(store = s)
		s.loc = places.__len__()
	template = "stores/list_stores.html"
	return render_to_response(template, {'stores': stores, 'user':request.user},context_instance=RequestContext(request))


@login_required
def store_form(request,id_store=None):
	"""
	CREATE OR EDIT A STORE
	"""
	if id_store:
		s = Store.objects.get(pk=id_store)
		#GET Places
		places = Place.objects.filter(store__pk__exact=id_store)
	else:
		s=Store()
	if request.method == 'POST': # If the form has been submitted...
		form = StoreForm(request.POST,instance=s) 
		if form.is_valid(): # All validation rules pass
			name = form.cleaned_data['name']
			description = form.cleaned_data['description']
			#Getting manager from current user
			manager = Manager.objects.get(user=request.user)
			form.save()
			if s:
				manager.store_set.add(s)
			more = request.POST.get('continue_inserting',False)
			#TODO: save places
			places = []
			for field in form.fields:
				if field.starts_with('place_'):
					places.append(form.fields[field])
			save_locations(s,places)
			if more == 'True' :
				redirection = "/store/new"
			else:
				redirection = '/store/edit/'+str(s.pk)
			return HttpResponseRedirect(redirection) # Redirect after POST
	else:
		form = StoreForm(instance=s)
	template='stores/store_form.html'
	places = {}
	return render(request, template, {
		'form': form,
		'pk' : id_store,
		'places' : places
	})

@login_required
def delete_store(request):
	"""
	Delete a store or list of stores
	"""
	if request.is_ajax:
		stores = request.GET.getlist('stores[]')
		try:
			Store.objects.filter(pk__in=stores).delete()
			message = _(u'Tiendas borradas correctamente')
		except:
			message = _(u'No se han podido borrar las tiendas')
			return HttpResponse(message, mimetype="text/plain")
		return HttpResponse(message, mimetype="text/plain")
	else:
		return HttpResponseForbidden()

@login_required
def get_subcategories(request):
	if not request.is_ajax():
		return HttpResponseForbidden()
	idcat = request.GET.get('idcategory')
	if idcat == None :
		return HttpResponseBadRequest()
	else:
		subcategories = serializers.serialize("json",Category.objects.filter(parent__id__exact=idcat))
		return HttpResponse(subcategories, mimetype="text/plain")

@login_required
def products(request, id_store, id_place = None):
	"""
	Store (or store localization) products view
	"""
	template = "products.html"
	data = {}
	return render_to_response(template, data, context_instance=RequestContext(request))

@login_required
def save_locations(store,places):
	"""
	Save a location (or a list) in a edited store. 
	For new store it come from store_form
	"""
	for p in places:
		"""
			split values.
			address;number;country;province;city;lat;lng;
		"""
		pieces = p.split(';')
		address = pieces[0]
		number = pieces [1]
		city = pieces [2]
		lat = pieces[3]
		lng = pieces[4]
		Place.city
		Place.address=pieces[0]

def load_place_form(request):
	place = request.GET.get('place',None)
	provinces_array = []
	if place is None or place is 'undefined':
		title = _(u'Nueva localización')
		provinces = Province.objects.all()
		for p in provinces:
			provinces_array.append({'name':p.name,'value' :p.id})
	else:
		title = _(u'Edita localización')
	data = {'title' : title,'provinces':provinces_array}
	template = 'places/partials/_place_form.html'
	return render_to_response(template, data, context_instance=RequestContext(request))


def get_countries(request):
	"""
		Load countries 
	"""
	countries = serializers.serialize("json",Country.objects.all())
	return HttpResponse(countries, mimetype="text/plain") 	

def get_provinces(request):
	idcountry=request.GET.get('idcountry',None)
	provinces = serializers.serialize("json",Province.objects.filter(country__id__exact=idcountry))
	return HttpResponse(provinces, mimetype="text/plain") 	


def get_cities(request):
	idprovince=request.GET.get('idprovince',None)
	cities = serializers.serialize("json",Province.objects.filter(province__id__exact=idprovince))
	return HttpResponse(cities, mimetype="text/plain") 	
