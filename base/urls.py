from django.urls import path
from .views import *
from blog.views import *

urlpatterns = [
    path('', Dashboard, name = "dashboard"),       

    path('login/', login_page ,name = "login"),
    path('logout/', logout_user ,name = "logout"),
    path('signup-patient/', signup_patient, name = "signup-patient"),
    path('signup-doctor/', signup_doctor, name = "signup-doctor"),

    path('blog/',BlogView, name = "blog"),
    path('upload-blog/', createBlog, name = "create-blog"),
    path('draft-blog/',draftBlog, name = "draft-blog"),
    path('update-draft-blog/', updateDraftBlog, name = "update-draft-blog"),
]
