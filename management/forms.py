from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Folder, File

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name']
        labels = {
            'name': 'Folder Name',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'file']
        labels = {
            'name': 'File Name',
            'file': 'Upload File',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
