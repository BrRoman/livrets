""" apps/main/views.py """

from django.shortcuts import render


def home(request):
    """ Home view of main app. """
    return render(request, 'main/home.html')
