from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_configuraciones, name='lista_configuraciones'),
    path('agregar/', views.agregar_configuracion, name='agregar_configuracion'),
    path('eliminar/<int:id>/', views.eliminar_configuracion, name='eliminar_configuracion'),
    path('modificar/<int:id>/', views.modificar_configuracion, name='modificar_configuracion'),
]
