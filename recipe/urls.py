
from django.urls import path, include
from accounts import views as accounts_views
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [

#    path('', views.recept, name='recept'),
    path('add_recipe', views.add_recipe, name='add_recipe'),
    path('<int:pk>/', views.ReceptDetailView.as_view(), name='recept_id'),
    path('user_recept', views.user_recept, name='user_recept'),

    path('update/<int:pk>', views.ReceptUpdateView.as_view(), name='update'),
    path('delete_recipe/<int:pk>', views.delete_recipe, name='delete_recipe'),
#    path('<int:pk>/delete_recipe/', views.ReceptUpdateView.as_view(), name='delete_recipe'),

    path('first_dish', views.first_dish, name = 'first_dish'),
    path('', views.second_dish, name = 'second_dish'),
    path('', views.salat, name = 'salat'),
    path('', views.dessert, name = 'dessert'),
    path('', views.drinks, name = 'drinks'),

#    path('home', views.PageBuilder, name='home'),

]
