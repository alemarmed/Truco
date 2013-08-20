# -*- coding: utf-8 -*-
'''
Created on 23/07/2013

@author: kamuisaeba
@author: alejandro
'''
from django.contrib.auth.decorators import login_required
from core.store.form import StoreForm, DiscountForm, ProductForm, LocationForm
from django.shortcuts import redirect, render_to_response
from django.template.context import RequestContext
from core.models import Manager, Store, City, Place, Category, Offer, Product,\
    Product_discount
from django.contrib import messages
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist


@login_required
def list_stores (request,template='store_list.html'):
    '''
    Listado basico de tiendas
    '''
    consumer = Manager.objects.get(user=request.user)
    stores = Store.objects.filter(owner=consumer)
    if request.GET.get('json',None):
        return HttpResponse(stores,mimetype="application/json")
    c = RequestContext(request,{'stores':stores})
    return render_to_response(template,c)


@login_required
def create_store (request,id_store=None):
    '''
    Create a new store
    '''
    template_name = "store.html"
    if id_store:
        try:
            store = Store.objects.get(pk=id_store)  
        except ObjectDoesNotExist as e:
            message = "La tienda no existe"
    else:
        store = None  
    form = StoreForm(request.POST or None,instance=store)
    if form.is_valid() and form.has_changed():
        store = form.save(commit=False)
        current_manager = Manager.objects.get(user=request.user)
        store.owner = current_manager
        store.save()
        message="OK"
        return redirect("/store/edit/"+str(store.pk))
    else:
        message="nook"
    return render_to_response(template_name,{'form':form,'message':message},context_instance=RequestContext(request))


@login_required
def delete_store (request,template='store_list.html'):
    '''
    Borra una tienda, por tanto sus localizaciones
    '''
    stores = request.GET.getlist('stores')
    stores_deleted = Store.objects.filter(pk__in=stores).delete()
    c = RequestContext(request)
    return redirect('/stores')


@login_required
def add_location (request,id_location=None,id_store=None):
    '''
    Crea una localización para una tienda, las coordenadas se calculan en el frontend 
    '''
    template_name = "location_add.html"
    initial = {}
    if request.is_ajax():
        lat = request.Get.get('latitude',None)
        lng = request.Get.get('longitude',None)
        address = request.Get.get('address',None)
        zip_code = request.Get.get('zip_code',None)
        store = Store.objects.get('idStore',None)
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
    else:
        location = None
        try:
            location = Place.objects.get(pk=id_location)  
        except ObjectDoesNotExist as e:
            message = "La localización no existe"
        location = location or None 
        store_pk = request.GET.get('store',None)
        if store_pk:
            try:
                store = Store.objects.get(pk=store_pk) or None
                initial['store']= store
            except ObjectDoesNotExist:
                pass            
        form = LocationForm(request.POST or None,instance=location,initial=initial)
        if form.is_valid() and form.has_changed():
            location = form.save(commit=False)
            current_manager = Manager.objects.get(user=request.user)
            store.owner = current_manager
            store.save()
            message="OK"
            return redirect("/store/location/list/")
        else:
            message="nook"
        return render_to_response(template_name,{'form':form,'message':message},context_instance=RequestContext(request))

@login_required
def create_product (request, idCategory):
    '''
    Ojo, las categorías tiene atributos, por tanto no todos los productos se crean con el mismo formulario
    '''
    template_name = "product.html"
    form = ProductForm(request.POST or None)
    if form.is_valid():
        product = form.save(commit=False)
        product.created_by(Manager.objects.get(user=request.user))
        product.save()

        message="OK"
        messages.add_message(request, messages.ERROR, message)
    else:
        message=="nook"
        messages.add_message(request, messages.SUCCESS, message)
    #TODO: asociar a tienda o localizacion
    return render_to_response(template_name,context_instance=RequestContext(request,{'form':form}))


@login_required
def create_discount (request):
    '''
    Fecha de validez y expiración
    '''
    template_name = "discount.html"
    form = DiscountForm(request.POST or None)
    if form.is_valid():
        discount = form.save()
        message="OK"
        messages.add_message(request, messages.ERROR, message)
    else:
        message=="nook"
        messages.add_message(request, messages.SUCCESS, message)
    return render_to_response(template_name,context_instance=RequestContext(request,{'form':form}))

@login_required
def add_discount (request):
    '''
    Asocia un descuento con uno/varios productos del usuario
    TODO: Cambiar modelos. ¿Permitimos más de una oferta para un producto? yo creo que deberíamos
    '''
    products = request.POST.getlist('product[]',None)
    discount = Offer.objects.get(request.POST.get('discount'))
    c = RequestContext(request,{})
    template = ""
    for p in products:
        #TODO: check if product is from any customer place
        try:
            product = Product.objects.get(p)
            product_discount = Product_discount(offer=discount,product=product)
            product_discount.save()
        except ObjectDoesNotExist as e:
            messages.add_message(request, messages.ERROR, "No existe el producto "+p)
        except Exception as e:
            messages.add_message(request.messages.ERROR,"Error al almacenar un descuento")
        finally:
            render_to_response(template,c)
    messages.add_message(request,messages.SUCCESS,"Los descuentos han sido almacenados")
    render_to_response(template,c)

@login_required
def remove_discount (request):
    '''
    Elimina un descuento para una seleccion de productos
    '''
    products = request.POST.getlist('product[]',None)
    discount = Offer.objects.get(request.POST.get('discount'))
    c = RequestContext(request,{})
    template = ""
    for p in products:
        #TODO: check if product is from any customer place
        try:
            product = Product.objects.get(p)
            Product_discount.objects.get(product=product,discount=discount).delete()
            status = 200
        except:
            status=500
    if request.is_ajax:
        return HttpResponse(status=status,mimetype="application/json")
    return render_to_response(template,c)
        
            

@login_required
def list_products (request):
    '''
    Listar los productos, filtro por localización/es, tienda, paginacion, categoria, marca...
    '''
    pass


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
def delete_location (request, idStore):
    '''
    Quita localizaciones de una tienda
    '''
    try:
        manager = Manager.objects.get(user=request.user)
        store = Store.objects.get(pk = request.GET.get('idStore'),owner=manager)
        Place.objects.filter(pk__in=request.GET.getlist('places',None),store=store).delete()
        message = "OK"
    except Exception:
        message = "NOOK"
    template = ""
    if request.is_ajax():
        return HttpResponse(message, mimetype="application/json")
    c = RequestContext(request,{'message':message})
    return render_to_response(template,c)

@login_required
def delete_discount (request):
    '''
    Borrar un descuento, hay que quitar las asociaciones que tenga con productos
    '''
    try:
        manager = Manager.objects.get(user=request.user)
        Offer.objects.filter(pk__in=request.GET.getlist('discounts',None),manager=manager).delete()
        message = "OK"
    except Exception:
        message = "NOOK"
    template = ""
    if request.is_ajax():
        return HttpResponse(message, mimetype="application/json")
    c = RequestContext(request,{'message':message})
    return render_to_response(template,c)


@login_required
def delete_product (request):
    '''
    '''
    try:
        manager = Manager.objects.get(user=request.user)
        
        #products = Product.objects.filter(pk__in=request.GET.getlist('products',None),manager=manager)
        #store = request.GET.getlist('store',None)
        #places = request.GET.getlist('place',None)
        #if store:
        #    products.filter(localization__store__in = store)
        #if places:
        #    products.filter(localization__in=places)
        #products.delete()
        message = "OK"
    except Exception:
        message = "NOOK"
    template = ""
    if request.is_ajax():
        return HttpResponse(message, mimetype="application/json")
    c = RequestContext(request,{'message':message})
    return render_to_response(template,c)

@login_required
def edit_store (request,id_store):
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
