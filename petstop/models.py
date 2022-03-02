from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Pet(models.Model):
    pet_name=models.CharField(max_length=40)
    type=models.CharField(max_length=40)
    breed=models.CharField(max_length=40)
    weight = models.FloatField()
    height = models.FloatField()
    color=models.CharField(max_length=40)
    age = models.IntegerField()
    description=models.CharField(max_length=300)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class Item(models.Model):
    item_name=models.CharField(max_length=40)
    mrp=models.FloatField()
    quantity=models.IntegerField()
    color=models.CharField(max_length=40)
    type=models.CharField(max_length=40)
    description= models.CharField(max_length=300)

class User_Detail(models.Model):
    age=models.IntegerField()
    email=models.CharField(max_length=40)
    address=models.CharField(max_length=40)
    phone = PhoneNumberField(max_length=15)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
