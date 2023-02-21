from django.db import models

# Create your models here.
class profile(models.Model):
    username=models.CharField(max_length=30, null=False)
    mobile=models.CharField(max_length=10)
    password=models.CharField(max_length=16)
