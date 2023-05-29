from __future__ import unicode_literals
from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField(max_length=200)
    body = models.TextField(max_length=10000)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    author = models.CharField(max_length=100, default='admin')
   

    def __str__(self):
        return self.title

