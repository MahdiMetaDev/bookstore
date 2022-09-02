from django.shortcuts import render
from django.views import generic
from django.contrib.auth import get_user_model

from .forms import UserCreationForm

class SignUpView(generic.CreateView):
    model = get_user_model()
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
