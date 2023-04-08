from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Main(models.Model):
    title = models.CharField(max_length=200)
    about = models.TextField(default='about')

    facebook = models.CharField(max_length=200, default='https://www.facebook.com/')
    twitter = models.CharField(max_length=200, default='https://twitter.com/')
    youtube = models.CharField(max_length=200, default='https://www.youtube.com/')
    instagram = models.CharField(max_length=200, default='https://www.instagram.com/')
    linkedin = models.CharField(max_length=200, default='https://www.linkedin.com/')
    github = models.CharField(max_length=200, default='https://github.com/')

    tel = models.CharField(max_length=200, default='tel:123456789')
    email = models.CharField(max_length=200, default='mailto:john.doe@example.com')
    link = models.CharField(max_length=200, default='https://example.com/')

    date = models.DateTimeField()
    #image = models.ImageField(upload_to='images/')

    set_title = models.CharField(max_length=200, default='News Mag')

    def __str__(self):
        return self.set_title + " | " + str(self.pk)

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.date.strftime('%b %e %Y')
