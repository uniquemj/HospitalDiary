from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender = Patient)
def create_patient_profile(sender, instance, created, **kwargs):
    print(sender)
    if created and instance.role == "PATIENT":
        PatientProfile.objects.create(user = instance)

@receiver(post_save, sender = Doctor)
def create_doctor_profile(sender, instance, created, **kwargs):
    if created and instance.role == "DOCTOR":
        DoctorProfile.objects.create(user = instance)