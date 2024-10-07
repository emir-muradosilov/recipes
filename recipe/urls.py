
from django.urls import path
from . import views


urlpatterns = [
#    path('', views.recept, name='recept'),
    path('add_recipe', views.add_recipe, name='add_recipe'),
    path('<int:pk>/', views.ReceptDetailView.as_view(), name='recept_id'),
    path('user_recept', views.user_recept, name='user_recept'),

    path('update/<int:pk>', views.ReceptUpdateView.as_view(), name='update'),
    path('delete_recipe/<int:pk>', views.delete_recipe, name='delete_recipe'),
#    path('<int:pk>/delete_recipe/', views.ReceptUpdateView.as_view(), name='delete_recipe'),
#    path('home', views.PageBuilder, name='home'),

]
