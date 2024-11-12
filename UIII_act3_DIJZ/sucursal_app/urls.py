from django.urls import path
from sucursal_app import views
urlpatterns = [
    path("",views.inicio_vista, name="inicio_vista"),
    path("registrarSucursal/",views.registrarSucursal,name="registrarSucursal"),
    path("seleccionarSucursal/<codigo>",views.seleccionarSucursal,name="seleccionarSucursal"),
    path("editarSucursal/",views.editarSucursal,name="editarSucursal"),
    path("borrarSucursal/<codigo>",views.borrarSucursal,name="borrarSucursal")
]