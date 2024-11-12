from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Recept(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    recept_name = models.CharField(max_length=255, blank=False)
    date = models.DateField(auto_now_add=True)
    recept_text = models.TextField(max_length=12000, blank=False)
    img = models.ImageField(upload_to='images/', blank=True)
    watched = models.IntegerField(default=0, blank=True)
    is_published = models.BooleanField(default=True, blank=True)
    category = models.ForeignKey(Category, default=1,on_delete=models.CASCADE, blank=True)
    # Поля title и description - технические поля для СЕО записи
    title = models.CharField(max_length=180)
    description = models.CharField (max_length=300, blank=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/recept/{self.id}'
    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class Comment(models.Model):
    recept = models.ForeignKey(Recept, on_delete=models.CASCADE, verbose_name='Рецепт')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    comment = models.TextField(max_length=1056, blank=True)
    date = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.comment
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'