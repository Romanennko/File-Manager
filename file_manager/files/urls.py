from django.urls import path
from . import views

urlpatterns = [
    path('', views.file_list, name='file_list'),
    path('upload/', views.upload_file, name='upload_file'),
    path('delete/<int:pk>/', views.delete_file, name='delete_file'),
    path('edit/<int:pk>/', views.edit_file, name='edit_file'),
]
