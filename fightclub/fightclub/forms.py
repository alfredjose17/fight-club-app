from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={"class": "form-group"}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"class": "form-group"}))

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={"class": "form-group"}))
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={"class": "form-group"}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={"class": "form-group"}))

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name')