# -*- coding: utf-8 -*-
from django.template.context import RequestContext
from django.http import HttpResponse, HttpResponseRedirect,\
	HttpResponseForbidden, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404, render_to_response,\
	redirect
from app.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from app.forms import StoreForm
from django.utils.simplejson import dumps
from django.utils.translation import ugettext as _

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
	template = "list_stores.html"
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
			return HttpResponseRedirect('/store/edit/'+str(s.pk)) # Redirect after POST
	else:
		form = StoreForm(instance=s)
	template='store_form.html'
	return render(request, template, {
		'form': form,
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
def products(request, id_store, id_place = None):
	"""
	Store (or store localization) products view
	"""
	template = "products.html"
	data = {}
	return render_to_response(template, data, context_instance=RequestContext(request))

@login_required
def save_location(request):
	"""
	Save a location in a edited store. 
	For new store it come from store_form
	"""

"""
	AJAX requests below
"""

@login_required
def get_subcategories(request):
	if not request.is_ajax():
		return HttpResponseForbidden();
	idcat = request.GET.get('idcategory');
	if idcat == None :
		return HttpResponseBadRequest();
	else:
		subcategories = Category.objects.filter(parent__pk__eq=idcat);
		return HttpResponse(dumps(subcategories));
	