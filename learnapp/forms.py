
from django import forms
from django.contrib.auth.models import User
from learnapp.models import UserDetails
from django_recaptcha.fields import ReCaptchaField

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserProfile(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['phone', 'address', 'street', 'city', 'zipcode', 'userpic']
