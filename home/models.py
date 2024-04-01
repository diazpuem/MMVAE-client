from django.db import models

def validate_file_extension_csv(value):
    if not value.name.endswith('.csv'):
        raise ValidationError(u'Error message')
    
def validate_file_extension_npz(value):
    if not value.name.endswith('.npz'):
        raise ValidationError(u'Error message')

class APIRequestInput(models.Model):
    csv = models.FileField(validators=[validate_file_extension_csv])
    npz = models.FileField(validators=[validate_file_extension_npz])
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
    
    