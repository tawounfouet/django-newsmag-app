from django.db import models

# Create your models here.


class SubCategory(models.Model):

    name = models.CharField(max_length=100)
    category_name = models.CharField(max_length=100, default='-')
    category_id = models.IntegerField(default=1)

    def __str__(self):
        return self.name

