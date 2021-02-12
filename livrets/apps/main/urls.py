""" apps/products/urls.py """

from django.urls import path, re_path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.home, name='home'),
]
