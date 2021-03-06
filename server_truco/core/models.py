# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db.utils import IntegrityError


class Category(models.Model):
	"""
	Categoria de los productos - only for admin panel
	"""
	name = models.CharField(max_length=256, help_text =_(u'Name of Category'), verbose_name =_(u'Name'))
	parent = models.ForeignKey('self', null=True, verbose_name =_(u"Parent Category"))
	visible = models.BooleanField(default = True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	
	def __unicode__(self):
		return "Category: "+self.name+" "+str(self.pk)
	
ATTR_TYPES = ( 	# TODO traducir esto
	('text', _(u'Texto')),
	('select', _(u'Selección')),
	('boolean',_(u'Boolean')),
	('numeric',_(u'Numero'))
)

class Category_attr(models.Model):
	"""
	Las categorías tienen diferentes atributos que se añadirán dinámicamente al formulario de los productos
	asignados a esta categoría (o sus hijos)
	"""
	name = models.CharField(max_length=256, verbose_name=_(u'Nombre'))
	type = models.CharField(max_length=256,verbose_name=_(u'Tipo de atributo'),choices=ATTR_TYPES)
	value = models.CharField(max_length=256,verbose_name=_(u'Valor/es'))
	is_required = models.BooleanField(default=True, verbose_name=_(u"Atributo requerido"))
	
class Consumer(models.Model):
	"""
	Usuario de la aplicacion movil
	"""
	user = models.OneToOneField(User)
	birthday = models.DateField(null=True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	token = models.CharField(max_length=256,null=True)
	token_expiration = models.DateTimeField(null=True)
	def __unicode__(self):
		return "Consumer: "+self.user.username+" "+str(self.pk)


class Manager(models.Model):
	"""
	Usuario gestor de establecimientos
	"""
	user = models.OneToOneField(User)
	nif = models.CharField(max_length = 10, help_text =_(u'NIF or passport'), verbose_name =_(u'Personal ID'))
	birthday = models.DateField(null=True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __unicode__(self):
		return "Manager: "+self.user.username+" "+str(self.pk)

class Store(models.Model):
	"""
	Establecimiento (p.e. nombre de una cadena de supermercados), puede tener varias ubicaciones
	"""
	name = models.CharField(max_length = 256, help_text =_(u'Name of Store'), verbose_name =_(u'Name'))
	description = models.TextField(null = True, help_text =_(u'Description'), verbose_name =_(u'Description'))
	"""
	Realmente es necesario un many to many aquí? se podría sacar y crear una relación de jerarquía
	de tienda en otro módulo aparte
	"""
	owner = models.ForeignKey(Manager, verbose_name = _(u'Store owners'))
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __unicode__(self):
		return "Store: "+self.name+" "+str(self.pk)

class Brand(models.Model):
	"""
	Marca de un producto
	"""
	name = models.CharField(max_length = 256, help_text =_(u'Name of Brand'), verbose_name =_(u'Name'))
	description = models.TextField(null = True, help_text =_(u'Description'), verbose_name =_(u'Description'))
	lowcost = models.BooleanField(default = False)
	property_of = models.ForeignKey(Store, null = True)
	def __unicode__(self):
		return "Brand: "+self.name+" "+str(self.pk)

"""
20132907-> deprecated por category_attr
class Tag(models.Model):
	Usado para añadir atributos a productos, (p.e. sin gluten, desnatado, ecologico)
	name = models.CharField(max_length=256, verbose_name =_(u'Tag'))
	description = models.TextField(null = True, verbose_name =_(u'Description'))
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __unicode__(self):
		return "Tag: "+self.name+" "+str(self.pk)
"""

SIZE_TYPES = ( 	# TODO traducir esto
	('mg', _(u'mili gramos')),
	('g', _(u'gramos')),
	('kg', _(u'kilo gramos')),
	('l', _(u'litros')),
	('cl', _(u'centi litros')),
	('ml', _(u'mili litros')),
	('p', _(u'pack')),
)


class Product(models.Model):
	"""
	Producto, representa un producto concreto localizado en al menos una tienda
	"""
	name = models.CharField(max_length = 256, help_text =_(u'Name of Product'), verbose_name =_(u'Name'))
	description = models.TextField(null = True, verbose_name =_(u'Description'))
	categories = models.ForeignKey(Category, verbose_name =_(u'Product category'))
	created_by = models.ForeignKey(Manager)
	#tags = models.ManyToManyField(Tag, verbose_name = _(u'Product attributes'))
	brand = models.ForeignKey(Brand, null = True)
	size_type = models.CharField(max_length=2, choices=SIZE_TYPES, null = True)
	size_amount = models.DecimalField(null = True, max_digits=10,decimal_places=2,verbose_name=_(u'Amount'))
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __unicode__(self):
		return "Product: "+self.name+" "+self.brand.name+" "+str(self.pk)



class Virtual_product(models.Model):
	"""
	Descripcion de un producto deseado por un usuario, no tiene que corresponder con ningun producto concreto
	"""
	name = models.CharField(max_length = 256, help_text =_(u'Name of Product'), verbose_name =_(u'Name'))
	description = models.TextField(null =True, help_text =_(u'Description'), verbose_name =_(u'Description'))
	categories = models.ForeignKey(Category, verbose_name =_(u'Product category'))
	#tags = models.ManyToManyField(Tag, verbose_name = _(u'Product attributes'))
	brand = models.ForeignKey(Brand, null = True)
	size_type = models.CharField(null = True, max_length=2, choices=SIZE_TYPES)
	size_amount = models.DecimalField(null = True, max_digits=10,decimal_places=2,verbose_name=_(u'Amount'))
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __unicode__(self):
		return "Virtual product: "+self.name+" "+str(self.pk)


class Country(models.Model):
	name = models.CharField(max_length=256, verbose_name=_(u'Country'))
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __unicode__(self):
		return "Country: "+self.name+" "+str(self.pk)


class Province(models.Model):
	name = models.CharField(max_length=256, verbose_name=_(u'Province'))
	country = models.ForeignKey(Country)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __unicode__(self):
		return "Province: "+self.name+" "+str(self.pk)


class City(models.Model):
	name = models.CharField(max_length=256, verbose_name=_(u'City'))
	province = models.ForeignKey(Province)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __unicode__(self):
		return "City: "+self.name+" "+str(self.pk)


class List(models.Model):
	"""
	Lista de la compra de un usuario
	"""
	name = models.CharField(max_length=256, help_text=_(u'Name of Product'),verbose_name=_(u'Name'))
	description = models.TextField(null = True, help_text =_(u'Description'), verbose_name =_(u'Description'))
	owner = models.ForeignKey(Consumer, related_name='my_lists')
	"""
	Sacarlo en otro módulo para tener más opciones?
	"""
	#shared_with = models.ManyToManyField(Consumer, related_name="shared_lists")
	routed = models.BooleanField(default = False)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __unicode__(self):
		return "List: "+self.name+" "+str(self.pk)


class List_item(models.Model):
	"""
	Elemento de una lista de la compra, puede ser un producto concreto o virtual.
	"""
	parent_list = models.ForeignKey(List)
	"""
	Si la lista se hace para una compra localizada, utilizamos productos reales
	"""
	product = models.ForeignKey(Product, null = True)
	"""
	Si la lista no está localizada, se le puede ofrecer una cierta flexibilidad
	"""
	vproduct = models.ForeignKey(Virtual_product, null = True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __unicode__(self):
		return "List item: "+self.product.name+" "+str(self.pk)
	
	def save(self, force_insert=False, force_update=False):
		if self.product is None and self.vproduct is None:
			raise IntegrityError(_('ERROR: product and vproduct can\'t be null at the same time '))
		# this can, of course, be made more generic
		models.Model.save(self, force_insert, force_update)

class Place(models.Model):
	"""
	Ubicacion de un establecimiento
	"""
	lat = models.DecimalField(max_digits=10,decimal_places=6,verbose_name=_(u'Latitude'))
	lng = models.DecimalField(max_digits=10,decimal_places=6,verbose_name=_(u'Longitude'))
	address = models.CharField(max_length=256, null=True,help_text=_(u'Address'),verbose_name=_(u'Address'))
	#Discuss if necessary
	zip_code = models.CharField(max_length = 50, verbose_name =_(u'Zip code'),null=True)
	store = models.ForeignKey(Store, verbose_name=_(u'Store'))
	city = models.ForeignKey(City, verbose_name=_(u'City'))
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __unicode__(self):
		return "Place: "+str(self.lat)+","+str(self.lng)


OFFER_TYPES = ( # TODO traducir esto
	('BT', _(u'Paga X Llevate Y')),
	('PD', _(u'Descuento del X%')),
	('UD', _(u'Unidad X al Y%')),
)
	
	
class Offer(models.Model):
	"""
	Representa una oferta o descuento aplicado al precio de un producto
	"""
	name = models.CharField(max_length = 256, help_text =_(u'Name'), verbose_name =_(u'Name'))
	text  = models.CharField(null = True, max_length = 256, help_text =_(u'Text'), verbose_name =_(u'Text'))
	date_from = models.DateField()
	date_to = models.DateField()
	manager = models.ForeignKey(Manager)
	offer_type = models.CharField(max_length=2, choices=OFFER_TYPES)
	x = models.DecimalField(null = True, max_digits=10,decimal_places=2,verbose_name=_(u'Amount'))
	y = models.DecimalField(null = True, max_digits=10,decimal_places=2,verbose_name=_(u'Amount'))
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __unicode__(self):
		return "Offer: "+self.name+" "+str(self.pk)


class Product_discount(models.Model):
	offer = models.ForeignKey(Offer)
	product = models.ForeignKey(Product)
	#¿PLACE?
	def __unicode__(self):
		return "Product "+self.product.name+" has offer "+self.offer.name

class Place_has_product(models.Model):
	"""
	Representa la venta de un producto en un lugar concreto con un precio
	NOTA: localization o store deben ser nulos
	"""
	localization = models.ForeignKey(Place, null  = True)
	store = models.ForeignKey(Store, null  = True)#Place ya tiene guardado store, pero es más fácil el borrado
	product = models.ForeignKey(Product)
	pvp = models.DecimalField(max_digits=10,decimal_places=2,verbose_name=_(u'Product PVP'))
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __unicode__(self):
		return "Place has product, id = "+str(self.pk)
	
	def save(self, force_insert=False, force_update=False):
		if self.store is None and self.localization is None:
			raise IntegrityError(_('ERROR al insertar: localization and store can\'t be null at the same time '))
		# this can, of course, be made more generic
		models.Model.save(self, force_insert, force_update)

#TODO: añadir usuarios a tiendas para que puedan modificar productos	
#Simplificar modelo place y store y dejar sólo la localización como una tienda?