from django.db import models


class Donor(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    BLOOD_TYPE_CHOICES = (
        ('A+', 'A Positive'),
        ('A-', 'A Negative'),
        ('B+', 'B Positive'),
        ('B-', 'B Negative'),
        ('AB+', 'AB Positive'),
        ('AB-', 'AB Negative'),
        ('O+', 'O Positive'),
        ('O-', 'O Negative'),
    )

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='donor/images', blank=True, null=True, default='')
    hospital = models.CharField(max_length=200, blank=True, null=True)
    organ_donated = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return f"{self.name} ({self.email})"
