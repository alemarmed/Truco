# Create your views here.
from django.template.context import RequestContext
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response

def home(request):
	template_name ='home.html'
	data = {}
	return render_to_response(template_name, data , context_instance=RequestContext(request))


def list_stores(request):
	pass


def store_form(request,id=None):
	pass