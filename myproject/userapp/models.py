from django.db import models

# Create your models here.
class UserData(models.Model):
    name = models.CharField(max_length=80)
    roll = models.IntegerField()
    city = models.CharField(max_length=80)
    