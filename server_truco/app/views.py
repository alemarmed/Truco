# -*- coding: utf-8 -*-
from django.template.context import RequestContext
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from app.models import *
from django.contrib.auth.decorators import login_required


def home(request):
	template ='home.html'
	data = {
		"count_users" : Consumer.objects.count(),
		"places" : Localization.objects.all()
	}
	return render_to_response(template, data , context_instance=RequestContext(request))


@login_required
def list_stores(request):
	"""
	List all store from a customer User
	"""

	#stores = Manager.objects.filter(store__owners__pk=request.user.pk)
	template = "list_stores.html"
	stores = []
	return render_to_response(template, {'stores': stores, 'user':request.user.manager})


#@login_required
def store_form(request,id_store=None):
	"""
	Form to create/edit stores from a customer User
	"""
	pass


#@login_required
def list_products(request,store):
	"""
	List all Products from a Customer User in a 
	"""
	pass


#TODO: Descomentar login_required cuando tengamos el registro
#@login_required
def product_form(request, store):
	"""
	Create a product in a customer store
	"""
	pass


