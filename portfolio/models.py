from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phone_number= models.CharField(max_length=10)
    description=models.TextField()