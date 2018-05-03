# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib import messages
from django.core.validators import RegexValidator
from django.core.urlresolvers import reverse
from django.core.validators import FileExtensionValidator
# Create your models here.
class Usuarios(models.Model):
    TIPOS_CIENTIFICOS={
        ('Matemático','Matemático'),
        ('Físico','Físico'),
    }
    Usuario=models.CharField(primary_key=True,max_length=20)
    contrasena=models.CharField(max_length=20)
    Carrera=models.CharField(max_length=20,choices=TIPOS_CIENTIFICOS)
    Nombres=models.CharField(max_length=35)
    Apellidos=models.CharField(max_length=35)
    correo_regex=RegexValidator(regex=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', message="Correo no válido")
    Correo=models.CharField(validators=[correo_regex],unique=True,max_length=60)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{13}$', message="Debes ingresar un número de 13 dígitos")
    CUI=models.CharField(validators=[phone_regex], max_length=17, blank=True)
    EstaActivo=models.CharField(max_length=20,default="No")
    def get_absolute_url(self):
        return reverse('usuario:detail', kwargs={'pk':self.pk})

class Textos(models.Model): 
    Name=models.CharField(max_length=20)
    Tex_id=models.AutoField(primary_key=True)
    Texto=models.FileField(upload_to="archivos", validators=[FileExtensionValidator(allowed_extensions=['pdf', 'pm2'])])


