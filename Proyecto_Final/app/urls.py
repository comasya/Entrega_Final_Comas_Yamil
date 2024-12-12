
from django.urls import path
from app import views

urlpatterns = [
    path('inicio/', views.inicio),
    path('contact/', views.contact),
    path('car/', views.car),
    path('blog/', views.blog),
    path('about/', views.about)    
]
