from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    date_of_birth = models.DateField()
    mobile_number = models.CharField(max_length=15, unique=True, null=True)
    address = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    specialty = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} - {self.specialty}"