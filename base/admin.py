from django.contrib import admin
from .models import *
# Register your model's here.

admin.site.register(User)
admin.site.register(PatientProfile)
admin.site.register(DoctorProfile)
