from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.
def login_page(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if not User.objects.filter(email = email).exists():
            messages.info(request,'User not found with this email !!')
            return redirect('login')

        user = authenticate(request, username = email, password = password)
        if user is None:
            messages.error(request,'Incorrect Password!!')
            return redirect('login')
        else:
            login(request,user)
            return redirect('dashboard')
            
    
    return render(request,'base/login-page.html')

def logout_user(request):
    logout(request)
    return redirect('login')

def signup_doctor(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        profile_picture = request.FILES.get('profile')
        line1 = request.POST.get('line1')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        

        if User.objects.filter(username = username).exists():
            messages.info(request,"Username already taken!!")
            return redirect('signup-doctor')

        if User.objects.filter(email = email).exists():
            messages.info(request,"Email with user exist!!")
            return redirect('signup-doctor')

        if password != confirm_password:
            messages.info(request, "Password and Confirm Password doesn't match ")
            return redirect('signup-doctor')
        

        doctor = Doctor(
            username = username, 
            first_name = first_name,
            last_name = last_name,
            email = email,
            profile_picture = profile_picture,
            line1 = line1,
            city = city,
            state = state,
            pincode = pincode
        )
        doctor.set_password(password)
        doctor.save()
        messages.success(request,"Doctor Registered!!")
        return redirect('login')
    return render(request,'base/signup-doctor.html')

def signup_patient(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        profile_picture = request.FILES.get('profile')
        line1 = request.POST.get('line1')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if User.objects.filter(username = username).exists():
            messages.info(request,"Username already taken!!")
            return redirect('signup-patient')

        if User.objects.filter(email = email).exists():
            messages.info(request,"Email with user exist!!")
            return redirect('signup-patient')
        
        if password != confirm_password:
            messages.info(request, "Password and Confirm Password doesn't match ")
            return redirect('signup-patient')

        patient = Patient(
            username = username, 
            first_name = first_name,
            last_name = last_name,
            email = email,
            profile_picture = profile_picture,
            line1 = line1,
            city = city,
            state = state,
            pincode = pincode
        )
        patient.set_password(password)
        patient.save()
        messages.success(request,"Patient Registered!!")
        return redirect('login')
    
    return render(request,'base/signup-patient.html')

@login_required(login_url='login')
def Dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    print(request.user.role)
    return render(request,'base/home.html')

