from django.urls import path
from . import views

urlpatterns = [
    path('', views.otpAuth),
    path('users/', views.usersList),
]