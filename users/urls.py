from django.urls import path
from .views import *



urlpatterns = [
    path('login/', login),
    path('register/', register),
    path('ninja/',template_ninja),
]