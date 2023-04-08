from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Main(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField()
    # image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.date.strftime('%b %e %Y')
