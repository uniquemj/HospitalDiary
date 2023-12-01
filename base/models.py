from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.

#Manager to filter user with Patient Role
class PatientManager(BaseUserManager):
    def get_queryset(self):
        results = super().get_queryset()
        return results.filter(role = User.Role.PATIENT)

#Manager to filter user with Patient Role
class DoctorManager(BaseUserManager):
    def get_queryset(self):
        results = super().get_queryset()
        return results.filter(role = User.Role.DOCTOR)
    
class User(AbstractUser):
    #Initializing Roles
    class Role(models.TextChoices):
        ADMIN = "ADMIN",'Admin'
        PATIENT = "PATIENT",'Patient'
        DOCTOR = "DOCTOR", 'Doctor'

    #Configuring base role of user model to be ADMIN
    base_role = Role.ADMIN

    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to="media/profile/")
    line1 = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)
    role = models.CharField(max_length=50, choices=Role.choices)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def save(self, *arg, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*arg, **kwargs)
        

#Patient Class which is a proxy class and it will set base_role to PATIENT
class Patient(User):
    base_role = User.Role.PATIENT

    class Meta:
        proxy = True

    get_patient = PatientManager()

class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.user.username}"

#Doctor Class which is a proxy class and it will set base_role to Doctor
class Doctor(User):
    base_role = User.Role.DOCTOR

    class Meta:
        proxy = True
    
    get_doctor = DoctorManager()

class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"