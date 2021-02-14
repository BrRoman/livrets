""" apps/accounts/views.py """

from django.contrib.auth.views import LoginView

from .forms import LivretsLoginForm


class LivretsLoginView(LoginView):
    """ Login view. """
    form_class = LivretsLoginForm
    template_name = 'accounts/login.html'
