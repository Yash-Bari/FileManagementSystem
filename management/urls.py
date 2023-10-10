from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Show login template by default
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),  # You can change 'home/' to a different URL for the home page
    path('create_folder/', views.create_folder, name='create_folder'),
    path('delete_folder/<int:folder_id>/', views.delete_folder, name='delete_folder'),
    path('upload_file/<int:folder_id>/', views.upload_file, name='upload_file'),
    # Add more URL patterns for other views as needed
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)