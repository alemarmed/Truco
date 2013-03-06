from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
# Create your models here


class Category(models.Model):
	name = models.CharField(max_length=256, help_text=_(u'Name of Category'),verbose_name=_(u'Name'))
	parent = models.ForeignKey(Category,null=True,verbose_name=_(u"Parent Category"))
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class Product(models.Model):
	name = models.CharField(max_length=256, help_text=_(u'Name of Product'),verbose_name=_(u'Name'))
	categories = models.ManyToManyField(Category,verbose_name=_(u'Product Categories'))
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    #localizations = models.ManyToManyField(Localization)


class Store (models.Model):
	name = models.CharField(max_length=256, help_text=_(u'Name of Product'),verbose_name=_(u'Name'))
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Place_has_product(models.Model):
	localization = models.ForeignKey(Localization)
	product = models.ForeignKey(Product)
	pvp = models.DecimalField(max_digits=10,decimal_places=2,verbose_name=_(u'Product PVP'))


class Manager(User):
	birthday = models.DateField(null=True)


class Consumer(User):
	birthday = models.DateField(null=True)	


class Localization(models.Model):
	lat = models.DecimalField(max_digits=10,decimal_places=6,verbose_name=_(u'Latitude')) 
	lng = models.DecimalField(max_digits=10,decimal_places=6,verbose_name=_(u'Longitude'))
	store = model.ForeignKey(Store,verbose_name=_(u'Store'))
	address = models.CharField(max_length=256, null=True,help_text=_(u'Address'),verbose_name=_(u'Address'))
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    #products = models.ManyToManyField(Product)


class List(models.Model):
	name = models.CharField(max_length=256, help_text=_(u'Name of Product'),verbose_name=_(u'Name'))
    """
    Lista de productos. Como lo ponemos?
    """
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    usuario = models.ForeignKey(User)


class 