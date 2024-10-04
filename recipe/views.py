from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Recept
from .forms import ReceptForms

from django.views.generic import UpdateView, DetailView, DeleteView

# Create your views here.

# Отображение всех рецептов
def recept(request):
    recipe = Recept.objects.all()
    return render(request, 'recipes.html',
                  {'recipe':recipe})

# Отображение конкретного рецепта по id (pk)
class ReceptDetailView(DetailView):
    #{{ object.recept_name }}
    model = Recept
    template_name = 'recipespage.html'


# Редактирование конкретного рецепта по id (pk)
class ReceptUpdateView(UpdateView):
    model = Recept
    template_name = 'update_recipe.html'
#    fields = ['recept_name','title','description','recept_text','img',]
    form_class = ReceptForms
    context_object_name = 'user_recept'

# Удаление конкретного рецепта по id (pk)
class ReceptDeleteView(DeleteView):
    model = Recept
    template_name = 'recipespage.html'
    context_object_name = 'recept'

# Отображение всех рецептов попользователя
def user_recept(request):
    recepts = Recept.objects.filter(author=request.user)
    return render(request, 'user_recept.html', {'user_recepts': recepts})

'''
def recept_id(request, pk):
    recipe = get_object_or_404(Recept, pk=pk)
    if request.method == 'GET':
        form = ReceptForms(instance=recipe)
        return render(request, 'recipespage.html', {'recipe': recipe, 'form': form})
    else:
        try:
            form = ReceptForms(request.POST, request.FILES, instance=recipe)
            form.save()
            return redirect('recipespage', {'recipe': recipe, 'form': form})
        except ValueError:
            return render(request, 'recipespage.html', {'recipe': recipe, 'form': ReceptForms(), })

'''

# Удаление рецепта по id
def delete_recipe(request, pk):
    recipe = Recept.objects.get(id=pk)
    if request.method == 'POST':
        recipe.delete()
    return redirect('user_recept', )


def edit_recept(request, pk):
    recipe = get_object_or_404(Recept, id=pk)
    if request.method == 'POST':
        recipe.datecompleted = timezone.now()
        recipe.save()
    return redirect('user_recept', )


def add_recipe(request):
    if request.method == 'GET':
        return render(request, 'add_recipe.html', {'ReceptForms': ReceptForms})
    if request.method == 'POST':
        try:
            form = ReceptForms(request.POST, request.FILES)
            print(request.POST['img'])
            if form.is_valid():
                new_recept = form.save(commit=False)
                new_recept.author = request.user
                new_recept.save()
                return redirect('recept')
        except ValueError as error:
            return render(request, 'add_recipe.html',
                          {'ReceptForms': ReceptForms, 'error': f'Ошибка. Введены некоректные данные! {error}'}, )
    else:
        return render(request, 'add_recipe.html', {'error': 'Что бы добавить рецепт нужно авторизоваться'})


