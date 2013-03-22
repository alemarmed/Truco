# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


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
		return self.name+" "+self.pk

class Consumer(models.Model):
	"""
	Usuario de la aplicacion movil
	"""
	user = models.OneToOneField(User)
	birthday = models.DateField(null=True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)


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
		return self.user.username+" "+str(self.pk)

class Store(models.Model):
	"""
	Establecimiento (p.e. nombre de una cadena de supermercados), puede tener varias ubicaciones
	"""
	name = models.CharField(max_length = 256, help_text =_(u'Name of Store'), verbose_name =_(u'Name'))
	description = models.TextField(help_text =_(u'Description'), verbose_name =_(u'Description'))
	owners = models.ManyToManyField(Manager, verbose_name = _(u'Store owners'))
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __unicode__(self):
		return self.name+" "+str(self.pk)

class Brand(models.Model):
	"""
	Marca de un producto
	"""
	name = models.CharField(max_length = 256, help_text =_(u'Name of Brand'), verbose_name =_(u'Name'))
	description = models.TextField(null = True, help_text =_(u'Description'), verbose_name =_(u'Description'))
	lowcost = models.BooleanField(default = False)
	property_of = models.ForeignKey(Store)


class Tag(models.Model):
	"""
	Usado para añadir atributos a productos, (p.e. sin gluten, desnatado, ecologico)
	"""
	name = models.CharField(max_length=256, verbose_name =_(u'Tag'))
	description = models.TextField(null =True, verbose_name =_(u'Description'))
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)


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
	description = models.TextField(null =True, verbose_name =_(u'Description'))
	categories = models.ManyToManyField(Category, verbose_name =_(u'Product categories'))
	tags = models.ManyToManyField(Tag, verbose_name = _(u'Product attributes'))
	brand = models.ForeignKey(Brand)
	size_type = models.CharField(max_length=2, choices=SIZE_TYPES)
	size_amount = models.DecimalField(null = True, max_digits=10,decimal_places=2,verbose_name=_(u'Amount'))
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)


class Virtual_product(models.Model):
	"""
	Descripcion de un producto deseado por un usuario, no tiene que corresponder con ningun producto concreto
	"""
	name = models.CharField(max_length = 256, help_text =_(u'Name of Product'), verbose_name =_(u'Name'))
	description = models.TextField(null =True, help_text =_(u'Description'), verbose_name =_(u'Description'))
	categories = models.ForeignKey(Category, verbose_name =_(u'Product category'))
	tags = models.ManyToManyField(Tag, verbose_name = _(u'Product attributes'))
	brand = models.ForeignKey(Brand)
	size_type = models.CharField(max_length=2, choices=SIZE_TYPES)
	size_amount = models.DecimalField(null = True, max_digits=10,decimal_places=2,verbose_name=_(u'Amount'))
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)


class Country(models.Model):
	name = models.CharField(max_length=256, verbose_name=_(u'Country'))
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)


class Province(models.Model):
	name = models.CharField(max_length=256, verbose_name=_(u'Province'))
	country = models.ForeignKey(Country)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)


class City(models.Model):
	name = models.CharField(max_length=256, verbose_name=_(u'City'))
	province = models.ForeignKey(Province)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)


class List(models.Model):
	"""
	Lista de la compra de un usuario
	"""
	name = models.CharField(max_length=256, help_text=_(u'Name of Product'),verbose_name=_(u'Name'))
	description = models.TextField(help_text =_(u'Description'), verbose_name =_(u'Description'))
	owner = models.ForeignKey(Consumer, related_name='my_lists')
	shared_with = models.ManyToManyField(Consumer, related_name="shared_lists")
	routed = models.BooleanField(default = False)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)


class List_item(models.Model):
	"""
	Elemento de una lista de la compra, puede ser un producto concreto o virtual.
	"""
	parent_list = models.ForeignKey(List)
	product = models.ForeignKey(Product, null = True)
	vproduct = models.ForeignKey(Virtual_product, null = True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)


class Localization(models.Model):
	"""
	Ubicacion de un establecimiento
	"""
	lat = models.DecimalField(max_digits=10,decimal_places=6,verbose_name=_(u'Latitude')) 
	lng = models.DecimalField(max_digits=10,decimal_places=6,verbose_name=_(u'Longitude'))
	address = models.CharField(max_length=256, null=True,help_text=_(u'Address'),verbose_name=_(u'Address'))
	zip_code = models.CharField(max_length = 50, verbose_name =_(u'Zip code'))
	store = models.ForeignKey(Store, verbose_name=_(u'Store'))
	city = models.ForeignKey(City, verbose_name=_(u'City'))
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)


class Offer(models.Model):
	"""
	Representa una oferta o descuento aplicado al precio de un producto
	"""
	OFFER_TYPES = ( # TODO traducir esto
		('BT', _(u'Paga X Llevate Y')),
		('PD', _(u'Descuento del X%')),
		('UD', _(u'Unidad X al Y%')),
	)
	name = models.CharField(null = True, max_length = 256, help_text =_(u'Name'), verbose_name =_(u'Name'))
	text  = models.CharField(max_length = 256, help_text =_(u'Text'), verbose_name =_(u'Text'))
	date_from = models.DateField()
	date_to = models.DateField()
	offer_type = models.CharField(max_length=2, choices=OFFER_TYPES)
	x = models.DecimalField(null = True, max_digits=10,decimal_places=2,verbose_name=_(u'Amount'))
	y = models.DecimalField(null = True, max_digits=10,decimal_places=2,verbose_name=_(u'Amount'))
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)


class Place_has_product(models.Model):
	"""
	Representa la venta de un producto en un lugar concreto con un precio
	"""
	localization = models.ForeignKey(Localization)
	product = models.ForeignKey(Product)
	pvp = models.DecimalField(max_digits=10,decimal_places=2,verbose_name=_(u'Product PVP'))
	offer = models.ForeignKey(Offer, null = True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
