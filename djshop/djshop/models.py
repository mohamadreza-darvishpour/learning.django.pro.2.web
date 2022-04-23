from django.db import models

#create models here

class products(models.Model):
    title = models.CharField(30)
    price = models.IntegerField()