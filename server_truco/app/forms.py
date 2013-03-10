#get the form from django-registration
from django.contrib.auth.models import User
from django import forms
from registration.forms import RegistrationForm
from django.utils.translation import ugettext_lazy as _
from app.models import *



class MyRegistrationForm(RegistrationForm):
	nif = forms.CharField(label =_(u'NIF or passport'))
	birthday = forms.DateField(label = _(u'Birthday'))

	def save(self, *args, **kwargs):
		new_user = super(MyRegistrationForm, self).save(*args, **kwargs)
		#put them on the User model instead of the profile and save the user
		new_user.nif = self.cleaned_data['nif']
		new_user.birthday = self.cleaned_data['birthday']
		new_user.save()

		#create a new profile for this user with his information

		#return the User model
		return new_user

