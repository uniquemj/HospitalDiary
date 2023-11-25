from django.urls import path
from .views import *

urlpatterns = [
    path('', Dashboard, name = "dashboard"),       

    path('login/', login_page ,name = "login"),
    path('logout/', logout_user ,name = "logout"),
    path('signup-patient/', signup_patient, name = "signup-patient"),
    path('signup-doctor/', signup_doctor, name = "signup-doctor"),
]
