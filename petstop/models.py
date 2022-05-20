from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Pet(models.Model):
    pet_name=models.CharField(max_length=40)
    type=models.CharField(max_length=40)
    breed=models.CharField(max_length=40)
    weight =ArrayField(models.IntegerField(null=True, blank=True), null=True, blank=True)
    height = models.FloatField()
    color=models.CharField(max_length=40)
    age = models.IntegerField()
    pet_pic=models.ImageField(null=True,blank=True)
    description=models.CharField(max_length=300)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class Item(models.Model):
    item_name=models.CharField(max_length=40)
    mrp=models.FloatField()
    item_pic=models.ImageField(null=True,blank=True)
    quantity=models.IntegerField(null=True,blank=True)
    color=models.CharField(max_length=40)
    type=models.CharField(max_length=40)
    description= models.CharField(max_length=300)

class User_Detail(models.Model):
    age=models.IntegerField()
    email=models.CharField(max_length=40)
    address=models.CharField(max_length=40)
    phone = PhoneNumberField(max_length=15)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

class Post(models.Model):
    pet_id=models.ForeignKey(Pet,on_delete=models.CASCADE)
    price=models.FloatField()
    description=models.CharField(max_length=300)

class Cart(models.Model):
    discount=models.FloatField()
    quantity=models.IntegerField()
    item=models.ForeignKey(Item,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

