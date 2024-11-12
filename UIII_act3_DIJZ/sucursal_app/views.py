from django.shortcuts import render

from .models import Sucursal

def inicio_vista(request):
    lassucursales=Sucursal.objects.all()
# Create your views here.
    return render(request,'gestionarSucursal.html',{"missucursales":lassucursales})



def registrarSucursal(request):
    id_sucursal=request.POST["numsucursal"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["numtelefono"]
    horario=request.POST["txthorario"]
    email=request.POST["txtemail"]
    ciudad=request.POST["txtciudad"]
    nombre=request.POST["txtnombre"]



    registrarSucursal=Sucursal.objects.create(id_sucursal=id_sucursal,nombre=nombre,direccion=direccion,telefono=telefono,horario=horario,email=email,ciudad=ciudad)
    

    
    return render

def seleccionarSucursal(request,id_sucursal):
    sucursal=Sucursal.objects.get(id_sucursal=id_sucursal)
    return render(request,"editarSucursal.html",{"misSUcursales":sucursal})


def editarSucursal(request):
    id_sucursal=request.POST["numsucursal"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["numtelefono"]
    horario=request.POST["txthorario"]
    email=request.POST["txtemail"]
    ciudad=request.POST["txtciudad"]
    nombre=request.POST["txtnombre"]

    sucursal=Sucursal.objects.get(id_sucursal=id_sucursal)
    sucursal.id_sucursal=id_sucursal
    sucursal.nombre=nombre
    sucursal.direccion=direccion
    sucursal.telefono=telefono
    sucursal.horario=horario
    sucursal.email=email
    sucursal.ciudad=ciudad
    sucursal.save()
    return render


def borrarSucursal(request,id_sucursal):
    sucursal=Sucursal.objects.get(id_sucursal=id_sucursal)
    sucursal.delete()

    return render
