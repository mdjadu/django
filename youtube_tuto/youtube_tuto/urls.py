"""youtube_tuto URL Configuration

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
from pages.views import home_view,render_view
from app1.views import product_detail_view,product_form_view,product_new_form_view,pure_django_form

urlpatterns = [
    path('', home_view, name='home'),
    path('render/',render_view),
    path('product/',product_detail_view),
    path('form/',product_form_view),
    path('new_form/',product_new_form_view),
    path('pure_form/',pure_django_form),
    path('admin/', admin.site.urls),
]
