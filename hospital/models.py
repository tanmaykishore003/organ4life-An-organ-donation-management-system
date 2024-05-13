from django.db import models

# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=20)
    hospital_image = models.ImageField(upload_to='hospital/images', blank=True, null=True, default='')
    # Add more fields as needed

    def __str__(self):
        return self.name
    




    