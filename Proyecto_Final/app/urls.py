
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
    path('form-con-api/',views.form_con_api, name="FormConApi")
    
]

urlpatterns += forms_api