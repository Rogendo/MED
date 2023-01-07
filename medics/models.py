from django.db import models
from django.apps import AppConfig

class Account(models.Model):
    profile=models.ImageField()
    Username=models.CharField(max_length=50)
    website=models.URLField(max_length=60)
    email=models.EmailField(max_length=20)
    # help_and_feedback=models.URLField()


