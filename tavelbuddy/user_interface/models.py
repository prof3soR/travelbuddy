from django.db import models

# Create your models here.
class profile(models.Model):
    username=models.CharField(max_length=30, null=False)
    mobile=models.CharField(max_length=10)
    password=models.CharField(max_length=16)
    def __str__(self):
        return "%s" % (self.username)

class destinations(models.Model):
    name=models.CharField(max_length=40)
    #images=models.FileField()
    type=models.CharField(max_length=20)
    season=models.CharField(max_length=20)
    festivals=models.CharField(max_length=100)
    secret_spot=models.CharField(max_length=100)
    todo=models.CharField(max_length=100)
    
class tripdetails(models.Model):
    username=models.ForeignKey(profile,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    destination=models.CharField(max_length=50)
    fromdate=models.DateField()
    duration=models.IntegerField()
    tripwith=models.CharField(max_length=20)
    interests=models.CharField(max_length=30)
    trip_itinerary=models.TextField()