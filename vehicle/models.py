from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Vehicle(models.Model):
    name = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=20)
    purchase_year = models.IntegerField()
    # owner = models.ForeignKey(User, related_name='vehicles', on_delete=models.CASCADE)

class Service(models.Model):
    vehicle = models.ForeignKey(Vehicle, related_name='services', on_delete=models.CASCADE)
    date = models.DateField()

class Petrol(models.Model):
    vehicle = models.ForeignKey(Vehicle, related_name='petrol', on_delete=models.CASCADE)
    amount = models.FloatField()
    liters = models.FloatField()
    date = models.DateField()

class Trip(models.Model):
    vehicle = models.ForeignKey(Vehicle, related_name='trips', on_delete=models.CASCADE)
    trip_date = models.DateField()
    kms_travelled = models.FloatField()

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     number = models.IntegerField(max_length=10)
#     address = models.CharField(max_length=200)
#
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance,created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

# Create your models here.
