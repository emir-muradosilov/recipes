from django.core.checks import messages
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Recept, Category, Comment
from .forms import ReceptForms, CommentForm

from django.views.generic import UpdateView, DetailView, DeleteView

# Create your views here.



# Отображение всех рецептов


# Отображение конкретного рецепта по id (pk)

class ClassReceptDetailView(DetailView):
    # Класс DetailView - отображния страницы рецепта и 3 рекомендации
    #{{ object.recept_name }}
    model = Recept
    template_name = 'recipespage.html'  # Укажите ваш шаблон
    context_object_name = 'recipt'  # Укажите имя контекста для текущего объекта
    def get_object(self, queryset=None):
        # Получаем объект рецепта по pk
        recipt = super().get_object(queryset)
        # Обновляем количество просмотров
        recipt.watched += 1
        recipt.save()
        return recipt
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получаем рекомендации
        context['recomendations'] = Recept.objects.filter(is_published=True).order_by('-watched')[:3]
        # Получаем комментарии
        context['comments'] = Comment.objects.filter(recept=self.object.pk)
        # Добавляем форму для комментариев
        context['CommentForm'] = CommentForm()
        print(context)
        return context

def ReceptDetailView(request, pk):
    # Метод DetailView - отображния страницы рецепта и 3 рекомендации
    try:
        recipt = Recept.objects.get(id = pk)
        q = recipt.watched + 1
        Recept.objects.filter(id = pk).update(watched=q)
        recomendations = Recept.objects.filter(is_published=True).order_by('-watched')[:3]
        comments = Comment.objects.filter(recept=pk)
#        messages.sucsess(request, 'Ваш комментарий добавлен')

        context = {
            'recomendations': list(recomendations),
            'CommentForm': CommentForm,
            'comments': comments,
            'recipt': recipt,
        }
        return render(request, 'recipespage.html', context)
    except ObjectDoesNotExist:
        pass
    except MultipleObjectsReturned:
        pass


def add_comment(request, pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.recept = Recept.objects.get(pk=pk)
#        comment.post = request.GET.get('comment')
#        print('Comment', comment)
        comment.save()
        return redirect('recept_id', pk)

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
    template_name = 'home.html'
    success_url ="home.html"
#    context_object_name = 'recept'


# Отображение всех рецептов пользователя
def user_recept(request):
    recipts = Recept.objects.filter(author=request.user)
    return render(request, 'user_recept.html', {'recipts': recipts})

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
    else:
        return redirect('home', )


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
            if form.is_valid():
                new_recept = form.save(commit=False)
                new_recept.author = request.user
                new_recept.save()
                return redirect('recept_id',new_recept.id)
        except ValueError as error:
            return render(request, 'add_recipe.html',
                          {'ReceptForms': ReceptForms, 'error': f'Ошибка. Введены некоректные данные! {error}'}, )
    else:
        return render(request, 'add_recipe.html', {'error': 'Что бы добавить рецепт нужно авторизоваться'})



def PageBuilder(request):
    recipts = Recept.objects.filter(is_published=True)
    categorys = Category.objects.filter(is_published=True)
    page = {
        'title': f"Главная страница",
        'recipts': recipts,
        'categorys': categorys,
#        'title': f"{category[pk].title}",
#        'description': f"{category[pk].description}",
    }
    return render(request, 'home.html', {'title': "Главная страница", 'recipts': recipts, 'categorys': categorys,})

def recomendations_method(request, kolvo:int):
    recomendations = Recept.objects.filter(is_published=True).order_by('-watched')[:kolvo]
    return render(request, '_post_recommendation.html',{'recomendate_recepts': recomendations})



