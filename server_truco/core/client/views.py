# -*- coding: utf-8 -*-
'''
Created on 23/07/2013

@author: kamuisaeba
'''
from django.contrib.auth.decorators import login_required

@login_required
def add_list (request):
    '''
    Create a new list
    '''
    pass


@login_required
def edit_list (request, idList = None):
    '''
    Edit a list
    '''
    pass


@login_required
def delete_list (request):
    '''
    Delete one or more lists
    '''
    pass


@login_required
def get_lists (request):
    '''
    Returns user's lists
    request.GET may have pagination parameters (start, limit)
    '''
    pass


@login_required
def toggle_list_done (request):
    '''
    Mark one or more lists
    '''
    pass


@login_required
def toggle_product_done (request, idList):
    '''
    Mark one or more products from a list
    '''
    pass


@login_required
def get_products (request, idCategory):
    '''
    Get available products in catalogues
    request.GET may have pagination parameters (start, limit)
    '''
    pass


@login_required
def add_product_to_list (request):
    '''
    Add a product to a list (or multiple lists)
    '''
    pass


@login_required
def edit_product_from_list (request):
    '''
    NICE TO HAVE, in a not so far future...
    Edit a user defined product from a list 
    '''
    pass


@login_required
def delete_product_from_list (request):
    '''
    Delete a product from a list
    '''
    pass


@login_required
def get_products_in_list (request, idList):
    '''
    Get products in a user list
    request.GET may have pagination parameters (start, limit)
    '''
    pass


@login_required 
def combine_lists (request):
    '''
    NICE TO HAVE
    '''
    pass


@login_required
def clone_list (request, idList):
    '''
    NICE TO HAVE
    '''
    pass

