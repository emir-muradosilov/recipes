from django.contrib import admin
from .models import Recept

# Register your models here.

class ReceptStyle(admin.ModelAdmin):
    list_display = ['id','title','date', 'author']
    list_display_links = ['id','title',]
    readonly_fields = ('date',)
    list_filter = ('date','author',)


admin.site.register(Recept, ReceptStyle)
