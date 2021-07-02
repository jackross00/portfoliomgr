from django.urls import path
from . import views

urlpatterns = [
    path('accounts/register/', views.register_page, name='register'),
    path('accounts/login/', views.login_page, name='login')
]