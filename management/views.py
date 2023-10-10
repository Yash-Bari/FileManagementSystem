from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Folder, File
from .forms import FolderForm, FileForm

def login_view(request):
    # Check if the user is already authenticated and redirect to the home page
    if request.user.is_authenticated:
        return redirect('home')  # Replace 'home' with your home page URL name

    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page after successful login
            else:
                error_message = "Invalid login credentials. Please try again."
        else:
            error_message = "Invalid form input. Please check the form fields."
    else:
        form = AuthenticationForm()  # Create a new login form for GET requests

    return render(request, 'login.html', {'form': form, 'error_message': error_message})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    folders = Folder.objects.filter(owner=request.user)
    return render(request, 'home.html', {'folders': folders})

@login_required
def create_folder(request):
    if request.method == 'POST':
        form = FolderForm(request.POST)
        if form.is_valid():
            folder = form.save(commit=False)
            folder.owner = request.user
            folder.save()
            messages.success(request, 'Folder created successfully!')
            return redirect('home')
    else:
        form = FolderForm()
    return render(request, 'create_folder.html', {'form': form})

@login_required
def delete_folder(request, folder_id):
    folder = get_object_or_404(Folder, pk=folder_id)
    if folder.owner == request.user:
        folder.delete()
        messages.success(request, 'Folder deleted successfully!')
    else:
        messages.error(request, 'You do not have permission to delete this folder.')
    return redirect('home')

@login_required
def upload_file(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id)
    
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the file and associate it with the folder
            file = form.save(commit=False)
            file.folder = folder
            file.save()
            return redirect('home')  # Redirect to the home page after successful upload
    else:
        form = FileForm()
    
    return render(request, 'upload_file.html', {'form': form, 'folder': folder})