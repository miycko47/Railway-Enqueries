from datetime import datetime
from django.db import models

# Create your models here.

class Booking(models.Model):
    roundtrip = models.BooleanField(default=True,blank=True)
    oneway = models.BooleanField(default=False,blank=True)
    multi_station = models.BooleanField(default=False,blank=True)
    
    departing = models.CharField(max_length=100, blank=False)
    destination = models.CharField(max_length=100, blank=False)
    departure_date = models.DateTimeField(default=datetime.now)
    return_date = models.DateTimeField(blank=True)
    
    adults = models.IntegerField(default=1,blank=True)
    children = models.IntegerField(default=0,blank=True)
    
    def __str__(self):
        return (self.departing)
    
    