# -*- coding: utf-8 -*-
#the pass of the superuser is pass1234 and the user is admin
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Problemas(models.Model): 
    numero = models.IntegerField(primary_key=True)
    documento=models.FileField()