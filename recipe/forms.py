from django.forms import ModelForm, TextInput, Textarea
from .models import Recept, Comment
from django import forms


class ReceptForms(ModelForm):
    class Meta:
        model = Recept
        fields = ['recept_name','title','description','recept_text', 'is_published', 'category', 'img',]

        widgets = {
            'recept_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название рецепта'
            }),
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок рецепта'
            }),
            'description': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Краткое описание рецепта'
            }),
            'recept_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Рецепт'
            }),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment', )

        widgets = {'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Оставьте ваш коментарий'
            })
            }

