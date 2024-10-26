import requests
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.views.generic import ListView

from recipe.models import Recept, Category
from django.core.paginator import Paginator

# Create your views here.


class SearchResultsView(ListView):
#    q = requests.get('q')
    model = Recept
    template_name = 'search.html'

    def get_result(self):
        q = self.requests.get('q')
        results = Recept.objects.filter(Recept(title=q))
        return results

def search(request):
    q = request.GET.get('q','')
    if q:
        # icontains для частичного совпадения
        results = Recept.objects.filter(title__icontains=q).order_by('date')
    else:
        results = Recept.objects.none()  # Если q пустой, возвращаем пустой QuerySet

    paginator = Paginator(results, 3)  # 5 объектов на странице
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    page = {
        'results': page_obj,  # Здесь используем page_obj
        'page_obj': page_obj,  # Также передаем сам объект пагинации для навигации
        'query': q,
    }

    return render(request, 'search.html', page,)

def PageBuilder(request):
    recipts = Recept.objects.filter(is_published=True).order_by('date')
    categorys = Category.objects.all()

    paginator = Paginator(recipts,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    page = {
        'title': f"Главная страница",
        'recipts': recipts,
        'categorys': categorys,
        'page_obj': page_obj,
    }
    return render(request, 'home.html', page)

def LeftMenu(request, pk):
    recipts = Recept.objects.filter(is_published=True, category=pk)
    categorys = Category.objects.all()

    paginator = Paginator(recipts,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    page = {
        'title': f"{Category.objects.get(id=pk)}",
        'recipts': recipts,
        'categorys': categorys,
        'page_obj': page_obj,
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
                user = authenticate(request, username=request.POST['username'], password=request.POST['password1'])
                login(request, user)
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

    elif (request.POST['login'] is not None) and ((request.POST["password1"] is not None) and (request.POST["password2"] is not None)):
        user = User.objects.create_user(username=request.POST['login'], password=request.POST['password1'])
        user.save()
        user = authenticate(request, username=request.POST['login'], password=request.POST['password1'])
        login(request, user)
        return redirect('home', )
    else:
        return render(request, {'error': 'Ошибка. Повторите ваш запрос позже!'})


