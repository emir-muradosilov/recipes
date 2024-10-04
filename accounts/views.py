from django.shortcuts import render, redirect
from django.contrib.auth.models import Permission, User
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.db import Error
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

from recipe.models import Recept


# Create your views here.


def home(request):
    recipe = Recept.objects.order_by('-date')[0:7]
    return render(request, 'home.html',{'recipe':recipe})


def registration_user(request):
    if request.method == 'GET':
        return render(request, 'registration\signup.html')
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST["username"], password=request.POST["password1"])
                user.save()
                return render(request, 'home.html')
            except IntegrityError:
                return render(request, 'registration\signup.html', {'error':'Это имя пользователя уже используется'})

        else:
                return render(request, {'error': 'Ошибка. Повторите ваш запрос позже!'})


def login_user(request):
    if request.method == 'GET':
        return render(request, 'registration\login.html')
    elif (request.POST['login'] is not None) and (request.POST["password"] is not None):
        user = authenticate(request, username=request.POST['login'], password=request.POST['password'])
        if user is None:
            return render(request, 'registration\login.html', {'error':'Такого пользователя не существует'})
        else:
            login(request, user)
            return render(request, 'home.html')
    else:
        return render(request, {'error': 'Ошибка. Повторите ваш запрос позже!'})

def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def signup(request):
    if request.method == 'GET':
        return redirect(request, 'registration/logout.html')
    else:
        return logout(request, 'home.html')


