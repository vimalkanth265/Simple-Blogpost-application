from django.db.models import fields
from django import forms
from django.forms.fields import EmailField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class userregister(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email','password1','password2']