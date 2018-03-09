# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django import forms
from models import Usuarios

class UserForm(forms.ModelForm):
    contrasena=forms.CharField(widget=forms.PasswordInput)
    class Meta: 
        model=Usuarios
        fields=['Usuario','Carrera', 'Nombres', 'Apellidos', 'Correo', 'CUI','contrasena']     