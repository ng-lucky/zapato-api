from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import *
from .models import *
from .serializers import *

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


class SignUpAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        # Logic to sign up a user
        email = request.data.get("email", "")
        password = request.data.get("password")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")

        if email == "":
            return Response({"detail": "Please provide email"}, status=HTTP_400_BAD_REQUEST)
        
        try:
            user = ZUser.objects.get(email=email)
            return Response({"detail": "Email already taken"}, status=HTTP_406_NOT_ACCEPTABLE)
        except ZUser.DoesNotExist:
            new_user = ZUser.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email
            )
            new_user.set_password(password)
            new_user.save()

            serializer = AuthSerializer(instance=new_user, many=False)

            return Response({"results": serializer.data, "message": "Account successfully created"}, status=HTTP_201_CREATED)



    @action(permission_classes=[IsAuthenticated], detail=False)
    def put(self, request):
        #logic to update a user's profile
        pass
class SignUpModelViewset(ModelViewSet):
    def sign_up(self, request):
        #logic to sign up user
        pass

