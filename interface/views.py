from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from .models import admindetail
import bcrypt
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request,'interface/signin.html')

def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        print(username, password)
        return redirect('home')
    else:
        return redirect('/')

def home(request):
    return render(request,'interface/index.html')


def encoding(request):
    username=input("Enter Username:")
    password = input("Enter Password:")
    password=password.encode('utf-8')

    hashed_passowrd=bcrypt.hashpw(password,bcrypt.gensalt())
    print(hashed_passowrd)
    user=admindetail(username=username,password=hashed_passowrd)
    user.save()
    return HttpResponse("<h1>Encoded</h1>")


def decoding(request):
    username=input("Enter Username:")
    password=input("Enter Password:")
    user=admindetail.objects.get(username=username)
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    print(hashed_password)
    if user!=None:
        if  not bcrypt.checkpw(str(user.password).encode('utf-8'),hashed_password):
            return HttpResponse("<h1>Decoded and Match's</h1>")
        else:
            return HttpResponse("<h1>Error</h1>")




