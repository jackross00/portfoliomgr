from django.urls import path
from . import views
from portfoliomgr import views as pm_vw

urlpatterns = [
    path('accounts/register/', views.register_page, name='register'),
    path('accounts/login/', views.login_page, name='login'),
    path('accounts/logout/', views.logout_user, name='logout_user'),
    path('', pm_vw.index, name='index')
]