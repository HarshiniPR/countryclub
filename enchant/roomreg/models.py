from django.db import models
# Create your models here.python manage.py

class Room (models.Model ):
    roomNo = models.IntegerField()
    roomType = models.CharField(max_length=200)
    noOfPeople = models.IntegerField()
    amount = models.IntegerField()
    vranda= models.IntegerField()

