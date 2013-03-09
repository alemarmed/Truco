# Create your views here.
from django.template.context import RequestContext
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from app.models import *

def home(request):
	template_name ='home.html'
	data = {}
	return render_to_response(template_name, data , context_instance=RequestContext(request))



#@login_required
def list_stores(request,id=None):
	"""
	List all store from a customer User
	"""
	stores = Store.objects.all()
	template = "list_stores.html"
	return render_to_response(template, {'stores': stores})


#@login_required
def store_form(request,id=None):
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


