from django.urls import path
from .views import *
from blog.views import *
from appointment.views import *

urlpatterns = [
    path('', Dashboard, name = "dashboard"),       

    #Base
    path('login/', login_page ,name = "login"),
    path('logout/', logout_user ,name = "logout"),
    path('signup-patient/', signup_patient, name = "signup-patient"),
    path('signup-doctor/', signup_doctor, name = "signup-doctor"),

    #Blog
    path('blog/',BlogView, name = "blog"),
    path('upload-blog/', createBlog, name = "create-blog"),
    path('draft-blog/',draftBlog, name = "draft-blog"),
    path('update-draft-blog/', updateDraftBlog, name = "update-draft-blog"),

    #Appointment
    path('doctors/',view_doctor, name = "doctors"),
    path('book-appointment/<str:username>/', book_appointment, name = "book-appointment"),
    path('confirmation-appointment/', confirm_appointment, name = "confirm-appointment"),
]
