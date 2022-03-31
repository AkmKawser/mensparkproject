from django.db import models
from django.contrib.auth.models import User

class Product (models.Model):
    product_name = models.CharField(max_length=100)
    product_img = models.ImageField(upload_to = 'pics/product')
    product_price = models.IntegerField()

class Outlet (models.Model):
    outlet_name = models.CharField (max_length=100)
    address = models.TextField()
    phone = models.IntegerField()
    manager_name = models.CharField(max_length=100)
    opentime = models.TextField()
    closetime = models.TextField()
    outlet_img = models.ImageField(upload_to = 'pics/outlet')
