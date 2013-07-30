'''
Created on 01/07/2013

@author: kamuisaeba
'''
from core.models import Consumer
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def register(request):
    """
    """
    return HttpResponse();


def facebook_login(request):
    pass


def google_login(request):
    pass


def twitter_login(request):
    pass

@login_required
def get_listas(request):
    """
    
    """
    user = Consumer.objects.filter(user=request.user)[0]
    pass

@login_required
def get_products(request):
    """
    """
    pass

@login_required
def save_lista(request):
    """
    """
    pass
    
@login_required
def save_product(request):
    """
    """
    pass
    