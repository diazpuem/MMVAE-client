from django.db import models

class APIRequestInput(models.Model):
    csv = models.FileField()
    npz = models.FileField()
    #+ "NPZ: " + self.npz


# Create your models here.
class RequestFilters(models.Model):
    id = models.AutoField(primary_key=True)
    organType = models.CharField(max_length=100)
    tissue = models.CharField(max_length=100)
    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.organType + " " + self.tissue