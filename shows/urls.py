from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='shows-home'),
    path('mode7/', views.mode7, name='shows-mode_7'),
    path('goldsoundz/', views.goldsoundz, name='shows-goldsoundz'),
]
