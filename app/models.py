from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    
    is_verified = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, blank=True, verbose_name="Phone Number")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, verbose_name="Gender")
    year_of_birth = models.PositiveIntegerField(blank=True, null=True, verbose_name="Year of Birth")
    
    def __str__(self):
        return self.username
      