from django.contrib.auth.models import AbstractUser
from django.db import models

SEX = (
    ('M', 'Male'),
    ('F', 'Female'),
)

class CustomUser(AbstractUser):
    occupation = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    sex = models.CharField(max_length=100, choices=SEX)
    
