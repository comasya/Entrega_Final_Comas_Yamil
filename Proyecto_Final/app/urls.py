
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
    path('autosform/', views.autos_form, name= 'AutosFormulario'),
    path('buscarautos/', views.buscar_autos, name= "BuscarAuto"),
    path('clientesform/', views.cliente_form, name= 'ClienteFormulario'),
    path('buscarcliente/', views.buscar_cliente, name= 'BuscarCliente'),
    path('alquilerform/', views.alquiler_form, name= "AlquilerFormulario"),
    path('buscar-alquiler/', views.buscar_alquiler, name= 'BuscarAlquiler'),
    path('autos_vbc/', views.AutosListView.as_view(), name= "ListaAutos"),
    path('autos_crear', views.AutosCreateView.as_view(), name= "CrearAutos"),
    path('autos_detalle/<pk>', views.AutosDetailView.as_view(), name= "DetalleAutos"),
    path('autos_editar/<pk>/editar', views.AutosUpdateView.as_view(), name= "EditarAutos"),
    path('autos_confirmar_borrar/<pk>/borrar', views.AutosDeleteView.as_view(), name= "BorrarAutos"),
    
]

urlpatterns += forms_api