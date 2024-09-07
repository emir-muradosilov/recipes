from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Recept

# Create your views here.

def recept(request):
    recipe = Recept.objects.all()
    return render(request, 'recipes.html',
                  {'recipe':recipe})


def recept_id(request, pk):
    recipe = get_object_or_404(Recept, pk=pk)
    return render(request, 'recipespage.html', {'recipe':recipe})



