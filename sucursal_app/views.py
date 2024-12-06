from django.shortcuts import render,redirect
from .models import Sucursal

# Create your views here.
def index_Sucursal(request):
    nSucursal=Sucursal.objects.all()
    return render(request,'gestSuc.html',{'lamp':nSucursal})

def regisSucursals(request): 
    id=request.POST["txtid"]
    nombre=request.POST["txtnom"]
    direc=request.POST["direc"]
    esp=request.POST["esp"]
    ins=request.POST["ins"]
    cant=request.POST["can"]
    enc=request.POST["enc"]
    
    guarSucursal=Sucursal.objects.create(
            id_sucursal=id,
            nombre=nombre,
            direccion=direc,
            espacio=esp,
            instrument=ins,
            cantidad=cant,
            encargado=enc, 
    )
    return redirect("Sucursal")

def selecSuc(request,id):
    suc=Sucursal.objects.get(id_sucursal=id)
    return render(request,'editarSuc.html',{"mSucursals":suc})

def editSuc(request):
    id=request.POST["txtid"]
    nombre=request.POST["txtnom"]
    direc=request.POST["direc"]
    esp=request.POST["esp"]
    ins=request.POST["ins"]
    cant=request.POST["can"]
    enc=request.POST["enc"]
    suc=Sucursal.objects.get(id_sucursal=id)
    suc.nombre=nombre
    suc.direccion=direc
    suc.espacio=esp
    suc.instrument=ins
    suc.cantidad=cant
    suc.encargado=enc
    suc.save()
    return redirect('Sucursal')

def borraSuc(request,id):
    suc=Sucursal.objects.get(id_sucursal=id)
    suc.delete()
    return redirect('Sucursal')