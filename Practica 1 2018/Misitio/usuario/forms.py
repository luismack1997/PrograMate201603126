# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from models import Usuarios
from models import Textos


class UserForm(forms.ModelForm):
    contrasena=forms.CharField(widget=forms.PasswordInput)
    class Meta: 
        model=Usuarios
        fields=['Usuario','Carrera', 'Nombres', 'Apellidos', 'Correo', 'CUI','contrasena']  

class TextForm(ModelForm):
    class Meta:
        model=Textos
        fields=['Name','Texto']   