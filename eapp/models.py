from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=30),
    password=models.CharField(max_length=30),

class user(models.Model):
    name = models.CharField(max_length=30),
    address = models.CharField(max_length=100),
    email = models.ForeignKey(login, on_delete=models.CASCADE)
    city = models.CharField(max_length=30)

class catagories(models.Model):
    product = models.CharField(max_length=30),
    quantity = models.CharField(max_length=30)

class product(models.Model):
    title = models.ForeignKey(catagories, on_delete=models.CASCADE)
    price = models.CharField(max_length=30),
    image_url = models.CharField(max_length=30)


