from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
import time
from django.contrib.auth.models import User


class Emergency(models.Model):
    name = models.CharField(max_length=30)

    phone = models.IntegerField(default=0)
    email = models.EmailField(max_length=30)
    Type_Of_Emergency = models.CharField(max_length=500)
    Exact_Location = models.CharField(max_length=100)
    Time_submitted = models.DateTimeField(auto_now_add=True)


class Updates(models.Model):
    update_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media', blank=True)
    video = models.FileField(upload_to='media', blank=True)


class Home(models.Model):
    content = models.TextField()


class Hospitals(models.Model):
    hospital_name = models.CharField(max_length=100)
    phone = models.IntegerField(default=0)
    email = models.EmailField(max_length=30)
    services = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    website = models.URLField()
    image = models.ImageField(upload_to='media', blank=True)
    hometown = models.CharField(max_length=100)


class FirstAid(models.Model):
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='media', blank=True)


class Map(models.Model):
    Area = models.CharField(max_length=1000)


#
# class Registration2(models.Model):
#
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     mobile=models.IntegerField(default=0)
#     email=models.EmailField(blank=True)
#     physical_address=models.CharField(max_length=100, blank=True)
#     home_town=models.CharField(max_length=50)
#     date_of_birth=models.DateField(default=time.timezone)
#     gender= models.CharField(max_length=20,blank=True)
#     pic = models.ImageField(upload_to='media', blank=True)
#     #
#     # @receiver(post_save,sender=User)
#     # def addons(sender,instance, created, **kwargs):
#     #     if created:
#     #         Registration2.objects.create(user=instance)
#     #     instance.registration2.save()


class Msgs(models.Model):
    name = models.CharField(max_length=25)
    phone = models.IntegerField()
    Email = models.EmailField(max_length=40)
    Subject = models.TextField(max_length=20)
    message = models.TextField(max_length=500)
    time_sent = models.DateTimeField(auto_now_add=True)


# Login and Reg models


class Profile(models.Model):
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phonenumber = models.IntegerField()
    dateofbirth = models.DateField(max_length=30)
    gender = models.CharField(choices=gender_choices,max_length=7)

    def __str__(self):
        return self.user.username
