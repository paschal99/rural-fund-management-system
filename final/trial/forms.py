from django import forms
from django.contrib.auth.forms import UserCreationForm
from django_select2.forms import Select2Widget
from .models.accont_model import *
from django.contrib.auth.forms import PasswordResetForm


class CustomPasswordResetForm(PasswordResetForm):
    def save(self, *args, **kwargs):
        # Custom save logic if necessary
        super().save(*args, **kwargs)


class UserRegistrationForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), widget=Select2Widget)
    role_choices = (
        ('member', 'Member'),
        ('administrative_secretary', 'Sponsor'),
        ('development_officer', 'Admin'),
    )
    sex_choices = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    POSITION_CHOICE = (
        ('mwenyekiti', 'mwenyekiti'),
        ('mtunza_hazina', 'mtunza_hazina'),
        ('mwanachama', 'mwanachama')
    )
    first_name = forms.CharField()
    last_name = forms.CharField()
    # password = forms.CharField()
    email = forms.EmailField()
    sex = forms.ChoiceField(choices=sex_choices, widget=forms.Select(attrs={'class': 'select2'}))
    phone = forms.CharField()
    # role = forms.ChoiceField(choices=role_choices, widget=forms.Select(attrs={'class': 'select2'}))
    position = forms.ChoiceField(choices=POSITION_CHOICE, widget=forms.Select(attrs={'class': 'select2'}))