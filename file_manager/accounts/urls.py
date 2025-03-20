from django.urls import path
from . import views
from .views import login_view

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
