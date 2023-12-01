from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class BookAppointment(models.Model):
    patient = models.ForeignKey(User, related_name="patient_appointment",on_delete= models.CASCADE)
    doctor = models.ForeignKey(User, related_name="doctor_appointment",on_delete= models.CASCADE)
    required_speciality = models.CharField(max_length=250)
    date_of_appointment = models.DateField()
    appointment_start_time = models.TimeField()
    appointment_end_time = models.TimeField()

    def __str__(self):
        return f'{self.patient}'

