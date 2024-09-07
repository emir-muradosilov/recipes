
from django.urls import path, include
from accounts import views as accounts_views
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.recept, name='recept'),
    path('<int:pk>/', views.recept_id, name='recept_id'),
    path('home', accounts_views.home, name = 'home'),
]
