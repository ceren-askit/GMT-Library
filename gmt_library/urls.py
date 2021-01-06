from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name = 'Home Page' ),
    path('academician/', views.academician , name = 'Academician Page' ),
]