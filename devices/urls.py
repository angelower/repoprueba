from django.urls import path
from . import views

urlpatterns = [
    path('devices/', views.index, name='index'),
]