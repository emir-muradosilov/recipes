
from django.urls import path
from . import views
from .views import ClassReceptDetailView

urlpatterns = [
#    path('', views.recept, name='recept'),
    path('add_recipe', views.add_recipe, name='add_recipe'),
#    path('<int:pk>/', views.ReceptDetailView, name='recept_id'),
    path('<int:pk>/', ClassReceptDetailView.as_view(), name='recept_id'),

    path('user_recept', views.user_recept, name='user_recept'),


    path('add_comment/<int:pk>/', views.add_comment, name='add_comment'),

    path('update/<int:pk>', views.ReceptUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.delete_recipe, name='delete'),
#    path('<int:pk>/delete/', views.ReceptDeleteView.as_view(), name='delete'),
#    path('home', views.PageBuilder, name='home'),

]
