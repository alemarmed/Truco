# -*- coding: utf-8 -*-
'''
Created on 23/07/2013

@author: alejandro
'''
from django.contrib.auth.decorators import login_required
from core.store.form import StoreForm
from django.shortcuts import redirect, render_to_response
from django.template.context import RequestContext
from core.models import Manager, Store, City, Place, Category
from django.contrib import messages
from django.http import HttpResponse

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
    lat = request.Get.get('latitude',None)
    lng = request.Get.get('longitude',None)
    address = request.Get.get('address',None)
    zip_code = request.Get.get('zip_code',None)
    store = Store.objects.get(idStore)
    city = request.Get.get('city',None)
    city_ = City.objects.get(city)
    try:  
        Place(lat=lat,lng=lng,zip_codes=zip_code,address=address,store=store,city=city_).save()
        messages.add_message(request, messages.SUCCESS, _(u'Añadida una' +
                +'nueva localización.'))
    except:
        messages.add_message(request, messages.SUCCESS, _(u'Fallo al Añadir una' +
                +'nueva localización a la tienda.'))
    c = RequestContext(request)
    return HttpResponse(c,mimetype="application/json")

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
    TODO: Cambiar modelos. ¿Permitimos más de una oferta para un producto? yo creo que deberíamos
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
def list_stores (request,template='/store_list.html'):
    '''
    Listado basico de tiendas
    '''
    consumer = Manager.objects.get(user=request.user)
    stores = Store.objects.filter(owners=consumer)
    if request.Get.get('json',None):
        return HttpResponse(stores,mimetype="application/json")
    return render_to_response(template,{'stores':stores})


@login_required
def list_locations (request, idStore):
    '''
    Listado de las localizaciones de una tienda
    '''
    template ="/location_list.html"
    places = Store.objects.get(idStore)
    if request.Get.get('json',None):
        return HttpResponse(places,mimetype="application/json")
    return render_to_response(template,{'stores':places})


@login_required
def delete_store (request):
    '''
    Borra una tienda, por tanto sus localizaciones
    '''
    stores = Store.objects.filter(pk__in=request.GET.getlist('stores[]')).delete()
    template =""
    c = RequestContext(request)
    return render_to_response(template,c)


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
    template = "categories.html"
    category = Category.objects.filter(parent_category)
    categories = Category.objects.filter(parent=category)
    if request.is_ajax():
        return HttpResponse(categories,mimetype="application/json")
    else:
        return render_to_response(template,categories,context_instance=RequestContext(request))

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
