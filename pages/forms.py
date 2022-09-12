from django import forms
from django.contrib.auth import get_user_model

from .models import Profile


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))

    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-control-file',
    }))

    bio = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 5,
    }))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']
