from django.shortcuts import render,redirect
from django.conf import settings
from base.models import *
from .models import *
from .helpers import *

import datetime

# Create your views here.



def view_doctor(request):
    doctors = Doctor.get_doctor.all()
    
    context = {
        'doctors': doctors
    }
    return render(request,'appointment/view_doctor.html',context)

def book_appointment(request, username):
    appointment_end_time = 0
    appointment_start_time = 0
    if request.method == "POST":
        required_speciality = request.POST.get('required_speciality')
        date_of_appointment = request.POST.get('date_of_appointment')
        start_time = request.POST.get('appointment_start_time')
        patient = Patient.get_patient.get(username = request.user.username)
        doctor = Doctor.get_doctor.get(username = username)
        doctor_email = doctor.email
        starts = date_of_appointment+' '+ start_time +':' '00'
        
        appointment_start_time = datetime.datetime.strptime(starts,"%Y-%m-%d %H:%M:%S")

        appointment_end_time  = appointment_start_time + datetime.timedelta(minutes = 45)



        BookAppointment.objects.create(
            patient = patient,
            doctor = doctor,
            required_speciality = required_speciality,
            date_of_appointment = date_of_appointment,
            appointment_start_time = appointment_start_time,
            appointment_end_time = appointment_end_time
        )

        print(appointment_start_time)
        print(appointment_end_time)
        calenderEvent(doctor_email, required_speciality, appointment_start_time, appointment_end_time)

        return redirect('confirm-appointment')
    
        
    return render(request,'appointment/book_appointment.html')


def confirm_appointment(request):
    record = BookAppointment.objects.filter(patient = request.user).last()
    return render(request,'appointment/confirm_appointment.html', context = {'record':record})