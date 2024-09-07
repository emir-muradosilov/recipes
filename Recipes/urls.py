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
from accounts import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('recept/', include('recipe.urls'), name='recept'),

#    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', views.login_user, name = 'login'),
    path('signup/', views.registration_user, name = 'signup'),
    path('logout/', views.logout_user, name = 'logout'),
    path('registration/', views.registration_user, name = 'registration'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)