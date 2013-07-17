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
				return redirect('home')
				# Redirect to a success page.
			else:
				# Return a 'disabled account' error message
				messages.add_message(request, messages.ERROR, _(u'Cuenta' +
				+'desactivada.'))
		else:
			# Return an 'invalid login' error message.

			messages.add_message(request, messages.ERROR,
								 _(u'El Usuario o Password no es válido.'))
			return render_to_response('registration/login.html',
							context_instance=RequestContext(request))
	return render_to_response('registration/login.html',
							context_instance=RequestContext(request))		
		# Return an 'invalid login' error message.


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
			if more == 'True' :
				redirection = "/store/new"
			else:
				redirection = '/store/edit/'+str(s.pk)
			return HttpResponseRedirect(redirection) # Redirect after POST
	else:
		form = StoreForm(instance=s)
	template='stores/store_form.html'
	return render(request, template, {
		'form': form,
		'pk' : id_store,
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
	data = {
		"pcategories" : Category.objects.filter(parent__exact=None,visible__exact=True)
	}
	if id_place is None:
		data['id_store'] = id_store
	else:
		data['id_place'] = id_place
	return render_to_response(template, data, context_instance=RequestContext(request))

@login_required
def save_location(request):
	"""
	Save a location in a edited store. 
	For new store it come from store_form
	"""
	pass

def load_place_form(request):
	place = request.GET.get('place',None)
	if place is None or place is 'undefined':
		title = _(u'Nueva localización')
	data = {'title' : title}
	template = 'stores/places/partials/_place_form.html'
	return render_to_response(template, data, context_instance=RequestContext(request))

def load_products(request):
	template = "_products_table.html"
	pk_store = request.GET.get('store', None)
	pk_place = request.GET.get('place', None)
	pk_category = request.GET.get('category', None)
	products = Product.objects.all()
	if pk_place is not None:
		products.filter(place_has_product__localization__pk__exact=pk_place)
	else:
		products.filter(place_has_product__store__pk__exact=pk_store)
	# TODO los productos que pertenezcan a categorias hijas deberian ser mostrados tambien
	products.filter(categories__category__pk__exact=pk_category)
	return render_to_response(template, {products : products}, context_instance=RequestContext(request))
	