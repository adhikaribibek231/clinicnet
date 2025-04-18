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
    
# class Staff(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     role = models.CharField(max_length=50, choices=[('admin', 'Admin'), ('receptionist', 'Receptionist')])
#     mobile_number = models.CharField(max_length=15, unique=True)
#     email = models.EmailField(unique=True)

#     def __str__(self):
#             return f"{self.first_name} {self.last_name} - {self.role.capitalize()}"
        
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('scheduled', 'Scheduled'), ('completed', 'Completed'), ('canceled', 'Canceled')])

    def __str__(self):
        return f"Appointment: {self.patient} with {self.doctor} on {self.appointment_date}"