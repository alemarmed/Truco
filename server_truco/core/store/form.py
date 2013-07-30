'''
Created on 30/07/2013

@author: antonio
'''
from django import forms
from core.models import Store, Manager
class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields= ["name","description"]
    def __init__(self,*args,**kwargs):
        super(StoreForm,self).__init__(*args,**kwargs)
        
        
        