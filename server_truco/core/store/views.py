# -*- coding: utf-8 -*-
'''
Created on 23/07/2013

@author: alejandro
'''
from django.contrib.auth.decorators import login_required
from core.store.form import StoreForm
from django.shortcuts import redirect, render_to_response
from django.template.context import RequestContext
from core.models import Manager

@login_required
def create_store (request):
    '''
    Create a new store
    '''
    template_name = "store.html"
    form = StoreForm(request.POST or None)
    if form.is_valid():
        store = form.save()
        current_manager = Manager.objects.get(user=request.user)
        store.owners.add(current_manager)
        store.save()
        message="OK"
    else:
        message="nook"
    return render_to_response(template_name,{'form':form,'message':message},context_instance=RequestContext(request))


@login_required
def add_location (request, idStore):
    '''
    Crea una localización para una tienda, las coordenadas se calculan en el frontend 
    '''
    pass


@login_required
def create_product (request, idCategory):
    '''
    Ojo, las categorías tiene atributos, por tanto no todos los productos se crean con el mismo formulario
    '''
    pass


@login_required
def create_discount (request):
    '''
    Fecha de validez y expiración
    '''
    pass


@login_required
def add_discount (request):
    '''
    Asocia un descuento con uno/varios productos del usuario
    '''
    pass


@login_required
def remove_discount (request):
    '''
    Elimina un descuento para una seleccion de productos
    '''
    pass


@login_required
def list_products (request):
    '''
    Listar los productos, filtro por localización/es, tienda, paginacion, categoria, marca...
    '''
    pass


@login_required
def list_stores (request):
    '''
    Listado basico de tiendas
    '''
    pass


@login_required
def list_locations (request, idStore):
    '''
    Listado de las localizaciones de una tienda
    '''
    pass


@login_required
def delete_store (request):
    '''
    Borra una tienda, por tanto sus localizaciones
    '''
    pass


@login_required
def delete_location (request, idStore):
    '''
    Quita localizaciones de una tienda
    '''
    pass


@login_required
def delete_discount (request):
    '''
    Borrar un descuento, hay que quitar las asociaciones que tenga con productos
    '''
    pass


@login_required
def delete_product (request):
    '''
    '''
    pass


@login_required
def edit_store (request):
    '''
    '''
    pass


@login_required
def edit_location (request):
    '''
    '''
    pass


@login_required
def edit_discount (request):
    '''
    '''
    pass


@login_required
def edit_product (request):
    '''
    '''
    pass


@login_required
def get_categories (request, parent_category = None):
    '''
    Obtener las cateogorías hijas de una dada, no recursivo
    '''
    pass


@login_required
def get_brands (request):
    '''
    '''
    pass


@login_required
def get_category_attributes (request, idCategory):
    '''
    Obtener los atributos propios y heredados de una categoría
    '''
    pass
