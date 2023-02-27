from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User


def login_user(request):
    if (request.method == 'POST'):
        login()
    return HttpResponse("<h1>Login Successful</h1>")

def register(request):
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        mesage = ''
        try:
            myuser = User.objects.get(email=email)
            message = "tis email already exists"
        except User.DoesNotExist:
            user = User.objects.create_user(username,email, password)
    return render(request, 'auth/register.html', {"message": message})

def template_ninja(request):
    return render(request, "ninja.html")