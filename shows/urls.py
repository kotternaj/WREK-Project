from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='shows-home'),
    path('Mode7/', views.mode7, name='shows-mode_7'),
    path('Goldsoundz/', views.goldsoundz, name='shows-goldsoundz'),
]
