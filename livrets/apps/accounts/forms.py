""" apps/accounts/forms.py """

from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LivretsLoginForm(AuthenticationForm):
    """ Login form of Livrets. """
    username = forms.CharField(
        label='Utilisateur :',
        initial='admin',
        error_messages={
            'required': 'Ce champ est obligatoire',
        }
    )
    password = forms.CharField(
        label='Entrez votre mot de passe :',
        error_messages={
            'required': 'Ce champ est obligatoire',
        },
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'autofocus': True}),
    )

    error_messages = {
        'invalid_login': 'Données non valides',
    }
