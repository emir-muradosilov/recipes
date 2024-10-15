from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from recipe.models import Recept, Category


# Create your views here.

def PageBuilder(request):
    recipts = Recept.objects.filter(is_published=True)
    categorys = Category.objects.all()
    page = {
        'title': f"Главная страница",
        'recipts': recipts,
        'categorys': categorys,
    }
    return render(request, 'home.html', page)

def LeftMenu(request, pk):
    recipts = Recept.objects.filter(is_published=True, category=pk)
    categorys = Category.objects.all()
    page = {
        'title': f"{Category.objects.get(id=pk)}",
        'recipts': recipts,
        'categorys': categorys,
    }
    return render(request, 'home.html', page)


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
            return redirect('home', )
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


