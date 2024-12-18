
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('contacto/', views.contact, name="Contacto"),
    path('vehiculos/', views.car, name="Vehiculos"),
    path('blog/', views.blog, name="Blog"),
    path('nosotros/', views.about, name="Nosotros")    
]
