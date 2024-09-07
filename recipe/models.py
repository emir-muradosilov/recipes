from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recept(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    recept_name = models.CharField(max_length=255, blank=False)
    title = models.CharField(max_length=100)
    description = models.CharField (max_length=1255, blank=False)
    date = models.DateField()
    recept_text = models.TextField(max_length=12000, blank=False)
    img = models.ImageField(upload_to='static/images/', blank=False)

    def __str__(self):
        return self.title