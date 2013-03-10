forms.py


#get the form from django-registration
from registration.forms import RegistrationForm

class MyRegistrationForm(RegistrationForm):
	nif = forms.CharField(max_length = 10, label =_(u'NIF or passport'), verbose_name =_(u'Personal ID'))
	birthday = forms.DateField(null=True,label = _(u'Birthday'))

    def save(self, *args, **kwargs):
        new_user = super(MyRegistrationForm, self).save(*args, **kwargs)
        #put them on the User model instead of the profile and save the user
        new_user.nif = self.cleaned_data['nif']
        new_user.birthday = self.cleaned_data['birthday']
        new_user.save()

        #create a new profile for this user with his information

        #return the User model
        return new_user