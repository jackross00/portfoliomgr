from django.urls import path
from . import views
from portfoliomgr import views as pm_vw

urlpatterns = [
    path('graphing/msci', views.msci, name='msci'),
    path('', pm_vw.index, name='index')
]