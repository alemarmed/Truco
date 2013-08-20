'''
Created on 30/07/2013

@author: antonio
'''
from django import forms
from core.models import Store, Manager, Offer, Product, Place_has_product, Place
from django.forms.widgets import Textarea
class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields= ["name","description"]
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 20}),
            }
    def __init__(self,*args,**kwargs):
        super(StoreForm,self).__init__(*args,**kwargs)
        
class DiscountForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields= ["name","text",'date_from','date_to',"offer_type","x","y"]
    def __init__(self,*args,**kwargs):
        super(StoreForm,self).__init__(*args,**kwargs)
        
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        
        
class LocationForm(forms.ModelForm):
     class Meta:
         model = Place      
        