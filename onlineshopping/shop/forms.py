from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,UserInfo

class UserForm(UserCreationForm):
    class Meta:
        model=UserInfo
        fields=['username','first_name','last_name','age','gender','contact','email','password1','password2']
