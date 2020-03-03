"""PLM_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from PLM import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='Home'),
    path('signup/', views.signup, name='SignUp'),
    path('login/', views.login, name='Login'),
    path('dashboard/', views.dashboard, name='Dashboard'),
    path('profile/', views.profile, name='Profile'),
    path('project-creation/', views.projectCreation, name='ProjectCreation'),
    path('about/', views.dashboard, name='About'),
    path('contact/', views.dashboard, name='Contact'),
    path('careers/', views.dashboard, name='Careers'),
    path('features/', views.dashboard, name='Features'),
    path('pricing/', views.dashboard, name='Pricing'),
    path('faq/', views.FAQ, name='FAQ'),
]
