
from django.urls import path
from app import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('contacto/', views.contact, name="Contacto"),
    path('vehiculos/', views.car, name="Vehiculos"),
    path('blog/', views.blog, name="Blog"),
    path('nosotros/', views.about, name="Nosotros")
       
]
forms_api = [
    path('autosform/', views.autos_form, name='AutosFormulario'),
    path('buscarautos/', views.buscar_autos, name="BuscarAuto"),
    path('clientesform/', views.cliente_form, name='ClienteFormulario'),
    path('buscarcliente/', views.buscar_cliente, name= 'BuscarCliente'),
    path('alquilerform/', views.alquiler_form, name="AlquilerFormulario"),
    path('buscar-alquiler/', views.buscar_alquiler, name= 'BuscarAlquiler')
    
]

urlpatterns += forms_api