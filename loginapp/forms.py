from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    workspace_id = forms.CharField(label='Workspace Id', widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class':'form-control'}))