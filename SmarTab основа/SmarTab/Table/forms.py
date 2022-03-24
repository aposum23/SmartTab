from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import  AuthenticationForm

from .models import *


class AuthUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'style':'height: 77px;width: 410px;background: #0F0F0E;border-style: none;margin-left: 95px;border-radius: 30px;'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'style':'width: 410px;height: 77px;background: #0F0F0E;border-style: none;margin-left: 95px;margin-top: px;border-radius: 30px;'}))


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'style': 'width: 247px;font-size: 20px;color: rgb(255,255,255);background: rgb(33,37,41);'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'style': 'width: 247px;font-size: 20px;color: rgb(255,255,255);background: rgb(33,37,41);'}))
    username = forms.CharField(widget=forms.TextInput(
        attrs={'style': 'width: 247px;font-size: 20px;color: rgb(255,255,255);background: rgb(33,37,41);'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'style': 'width: 247px;font-size: 20px;color: rgb(255,255,255);background: rgb(33,37,41);'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'style': 'width: 247px;font-size: 20px;color: rgb(255,255,255);background: rgb(33,37,41);'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')
        widgets = {
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'username': forms.TextInput(),
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }