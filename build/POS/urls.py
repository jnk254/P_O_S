
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.login,name='login'),
    path('password.html',views.resetpassword,name='password'),
    path('register.html',views.register,name='register'),
    path('home.html',views.home,name='home'),
    
]