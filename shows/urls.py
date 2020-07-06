from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='shows-home'),
    path('mode_7/', views.mode_7, name='shows-mode_7'),    
]
