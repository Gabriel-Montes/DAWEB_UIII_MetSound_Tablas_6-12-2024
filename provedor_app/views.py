from django.shortcuts import render,redirect
from .models import Provedor

# Create your views here.
def index_Provedor(request):
    nProvedor=Provedor.objects.all()
    return render(request,'gestPro.html',{'lamp':nProvedor})

def regisProvedors(request): 
    id=request.POST["txtid"]
    nombre=request.POST["txtnom"]
    cant=request.POST["can"]
    fent=request.POST["fen"]
    tell=request.POST["tel"]
    est=request.POST["est"]
    ins=request.POST["ins"]
    
    guarProvedor=Provedor.objects.create(
            id_prove=id,
            nombre=nombre,
            cantidad=cant,
            fecha_entre=fent,
            telefono=tell,
            estado=est,
            instrument=ins
    )
    return redirect("Provedor")

def selecPro(request,id):
    pro=Provedor.objects.get(id_prove=id)
    return render(request,'editarPro.html',{"mProvedors":pro})

def editPro(request):
    id=request.POST["txtid"]
    nombre=request.POST["txtnom"]
    cant=request.POST["can"]
    fent=request.POST["fen"]
    tell=request.POST["tel"]
    est=request.POST["est"]
    ins=request.POST["ins"]
    pro=Provedor.objects.get(id_prove=id)
    pro.nombre=nombre
    pro.cantidad=cant
    pro.fecha_entre=fent
    pro.telefono=tell
    pro.estado=est
    pro.instrument=ins
    pro.save()
    return redirect('Provedor')

def borraPro(request,id):
    pro=Provedor.objects.get(id_prove=id)
    pro.delete()
    return redirect('Provedor')