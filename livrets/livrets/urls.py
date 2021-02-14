""" urls.py """

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('livrets/', include('apps.main.urls')),
    path('livrets/accounts/', include('apps.accounts.urls')),
    path('livrets/admin/', admin.site.urls, name='admin'),
]
