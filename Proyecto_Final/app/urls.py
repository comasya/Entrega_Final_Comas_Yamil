
from django.urls import path
from app import views

urlpatterns = [
    path('inicio/', views.inicio),
    path('celulares/',views.Telefono),
    path('clientes/',views.Cliente),
    path('ventas/',views.Venta)
]
