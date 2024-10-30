from django.contrib import admin
from .models import Recept
from .models import Category, Comment
# Register your models here.

class ReceptStyle(admin.ModelAdmin):
    list_display = ['id','title','date', 'author', 'is_published']
    list_display_links = ['id','title',]
    readonly_fields = ('date',)
    list_filter = ('date','author',)
    list_editable = ('is_published',)
    readonly_fields = ('watched',)


admin.site.register(Recept, ReceptStyle)
admin.site.register(Category)

admin.site.register(Comment)


