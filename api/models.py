# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Note(models.Model):
    number = models.CharField(max_length=15)
    name = models.CharField(max_length=40)
    typefacc = models.CharField(max_length=5)
def __str__(self):
        return self.number