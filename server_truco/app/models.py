from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class Brand(models.Model):
	name = models.CharField(max_length = 256, help_text =_(u'Name of Brand'), verbose_name =_(u'Name'))
	description = models.TextField(null = True, help_text =_(u'Description'), verbose_name =_(u'Description'))
	lowcost = models.BooleanField(default = False)
	property_of = models.ForeignKey(Store)


class Category(models.Model):
	"""
	only for admin panel
	"""
	name = models.CharField(max_length=256, help_text =_(u'Name of Category'), verbose_name =_(u'Name'))
	parent = models.ForeignKey(Category,null=True, verbose_name =_(u"Parent Category"))
	visible = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class City(models.Model):
	name = models.CharField(max_length=256, verbose_name=_(u'City'))
	province = models.ForeignKey(Province)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class Consumer(User):
	birthday = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class Country(models.Model):
	name = models.CharField(max_length=256, verbose_name=_(u'Country'))
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class List(models.Model):
	name = models.CharField(max_length=256, help_text=_(u'Name of Product'),verbose_name=_(u'Name'))
	description = models.TextField(help_text =_(u'Description'), verbose_name =_(u'Description'))
    owner = models.ForeignKey(Consumer)
    shared_with = models.ManyToManyField(Consumer)
    routed = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class List_item(models.Model):
	parent_list = models.ForeignKey(List)
	product = models.ForeignKey(null = True, Product)
	vproduct = models.ForeignKey(null = True, Virtual_product)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Localization(models.Model):
	lat = models.DecimalField(max_digits=10,decimal_places=6,verbose_name=_(u'Latitude')) 
	lng = models.DecimalField(max_digits=10,decimal_places=6,verbose_name=_(u'Longitude'))
	address = models.CharField(max_length=256, null=True,help_text=_(u'Address'),verbose_name=_(u'Address'))
	zip_code = models.CharField(max_length = 50, verbose_name =_(u'Zip code'))
	store = model.ForeignKey(Store, verbose_name=_(u'Store'))
	city = models.ForeignKey(City, verbose_name=_(u'City'))
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class Manager(User):
	nif = models.CharField(max_length = 10, help_text =_(u'NIF or passport'), verbose_name =_(u'Personal ID'))
	birthday = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class Offer(models.Model):
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
	localization = models.ForeignKey(Localization)
	product = models.ForeignKey(Product)
	pvp = models.DecimalField(max_digits=10,decimal_places=2,verbose_name=_(u'Product PVP'))
	offer = models.ForeignKey(Offer, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class Product(models.Model):
	SIZE_TYPES = ( 	# TODO traducir esto
		('mg', _(u'mili gramos')),
		('g', _(u'gramos')),
		('kg', _(u'kilo gramos')),
		('l', _(u'litros')),
		('cl', _(u'centi litros')),
		('ml', _(u'mili litros')),
		('p', _(u'pack')),
	)
	name = models.CharField(max_length = 256, help_text =_(u'Name of Product'), verbose_name =_(u'Name'))
	description = models.TextField(null =True, verbose_name =_(u'Description'))
	categories = models.ManyToManyField(Category, verbose_name =_(u'Product categories'))
	tags = models.ManyToManyField(Tag, verbose_name = _(u'Product attributes'))
	brand = models.ForeignKey(Brand)
	size_type = models.CharField(max_length=2, choices=SIZE_TYPES)
	size_amount = DecimalField(null = True, max_digits=10,decimal_places=2,verbose_name=_(u'Amount'))
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class Province(models.Model):
	name = models.CharField(max_length=256, verbose_name=_(u'Province'))
	country = models.ForeignKey(Country)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class Store (models.Model):
	name = models.CharField(max_length = 256, help_text =_(u'Name of Store'), verbose_name =_(u'Name'))
	description = models.TextField(help_text =_(u'Description'), verbose_name =_(u'Description'))
	owners = models.ManyToManyField(Manager, verbose_name = _(u'Store owners'))
    localizations = models.ManyToManyField(Localization, verbose_name = _(u'Localizations'))
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class Tag(models.Model):
	name = models.CharField(max_length=256, verbose_name =_(u'Tag'))
	description = models.TextField(null =True, verbose_name =_(u'Description'))
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class Virtual_product(models.Model):
	name = models.CharField(max_length = 256, help_text =_(u'Name of Product'), verbose_name =_(u'Name'))
	description = models.TextField(null =True, help_text =_(u'Description'), verbose_name =_(u'Description'))
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
