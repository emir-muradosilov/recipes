"""
URL configuration for Recipes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from Recipes.settings import DEBUG
from accounts import views
from django.conf.urls.static import static
from django.conf import settings

from accounts.views import SearchResultsView, ReceptList, ReceptDetail, CategoryDetail, CategoryList

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.PageBuilder, name='home'),
    path('<int:pk>', views.LeftMenu, name='category'),
#    path('search/', views.search, name='search'),
    path('search/', views.search, name='search'),
#    path('', include('recipe.urls'), name='home'),

# Работа с рецептами
    path('recept/', include('recipe.urls'), name='recept'),
    path('recept/', include('recipe.urls'), name='add_recipe'),
    path('recept/', include('recipe.urls'), name = 'user_recept'),
    path('<int:pk>/delete/', include('recipe.urls'), name='delete'),
    path('update/<int:pk>/', include('recipe.urls'), name='update'),
#    path('update/<int:pk>/', views.ReceptUpdateView.as_view(), name='update'),
    path('add_comment/<int:pk>/', include('recipe.urls'), name='add_comment'),


# Регистрация и Аутентификация
    path('login/', views.login_user, name = 'login'),
    path('signup/', views.registration_user, name = 'signup'),
    path('logout/', views.logout_user, name = 'logout'),
    path('registration/', views.registration_user, name = 'registration'),

    path('user/', views.user, name = 'user'),

    # API по рецептам
    path('apiresept/api/', ReceptList.as_view(), name='apiresept-list'),
    path('apiresept/api/<int:pk>/', ReceptDetail.as_view(), name='apiresept-detail'),
    # API по Категории
    path('apicategory/api/', CategoryList.as_view(), name='apicategory-list'),
    path('apicategory/api/<int:pk>/', CategoryDetail.as_view(), name='apicategory-detail'),

]
if DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
