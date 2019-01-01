# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    mobile = models.CharField(max_length=15)
    fname = models.CharField(max_length=20)
    fname = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    status =models.CharField(max_length=5)
    