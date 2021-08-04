# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime

class Contact_Us(models.Model):
    
    id =  models.AutoField(primary_key=True)
    name = models.CharField('Name', max_length=50, blank=False, null=False)
    email = models.EmailField('Email', max_length=254)
    message = models.TextField('Message',max_length=254, blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Client: ' + str(self.name)

    class Meta:
        managed = True
        verbose_name =  'Contact_Us'
        verbose_name_plural =  'Contact_Us'


class about_me(models.Model):
    bout_me = models.TextField('About_me',blank=True, null=True, max_length=1500)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bout_me

    class Meta:
        managed = True
        verbose_name =  'About_me'
        verbose_name_plural =  'About_me'

class cvUpload(models.Model):
    file_name = models.CharField('File Name', blank=True, null=True, max_length=50)
    file_uploaded = models.FileField('File Upload', upload_to='media')

    def __str__(self):
        return self.file_name