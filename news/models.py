from __future__ import unicode_literals
from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField(max_length=200)
    body = models.TextField(max_length=10000)
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    #date = models.DateTimeField(default='0000-00-00')
    time = models.TimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(upload_to='./', blank=True, null=True)
    image_url = models.CharField(max_length=200, default='-')
    author = models.CharField(max_length=100, default='admin')
    category = models.CharField(max_length=100, default='-')
    category_id = models.IntegerField(default=1)
    ocategory_id = models.IntegerField(default=1)
    
    show = models.IntegerField(default=0)

    def __str__(self):
        return self.title

