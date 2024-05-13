from django.db import models

class Patient(models.Model):
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

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
        ('Accepted', 'Accepted'),
    )

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    medical_condition = models.TextField()
    organ_needed = models.CharField(max_length=100)
    urgency_level = models.IntegerField(default=1, help_text="1: Least Urgent, 10: Most Urgent")
    date_added = models.DateTimeField(auto_now_add=True)
    donor_name = models.CharField(max_length=100, default='')
    hospital = models.CharField(max_length=100, default='')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return self.name
