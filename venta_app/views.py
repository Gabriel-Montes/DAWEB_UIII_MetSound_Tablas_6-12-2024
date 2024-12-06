from django.shortcuts import render,redirect
from .models import Venta

# Create your views here.
def index_Venta(request):
    nVenta=Venta.objects.all()
    return render(request,'gestVen.html',{'lamp':nVenta})

def regisVentas(request): 
    id=request.POST["txtid"]
    cant=request.POST["can"]
    ins=request.POST["ins"]
    pre=request.POST["pto"]
    suc=request.POST["csu"]
    cli=request.POST["cli"]
    emp=request.POST["emp"]
    
    guarVenta=Venta.objects.create(
            id_venta=id,
            cantidad=cant,
            instrument=ins,
            precio_tot=pre,
            id_cliente=cli,
            id_sucursal=suc,
            id_empleado=emp,
    )
    return redirect("Venta")

def selecVen(request,id):
    suc=Venta.objects.get(id_venta=id)
    return render(request,'editarVen.html',{"mVentas":suc})

def editVen(request):
    id=request.POST["txtid"]
    cant=request.POST["can"]
    ins=request.POST["ins"]
    pre=request.POST["pto"]
    suc=request.POST["csu"]
    cli=request.POST["cli"]
    emp=request.POST["emp"]
    ven=Venta.objects.get(id_venta=id)
    ven.cantidad=cant
    ven.instrument=ins
    ven.precio_tot=pre
    ven.id_cliente=cli
    ven.id_sucursal=suc
    ven.id_empleado=emp
    ven.save()
    return redirect('Venta')

def borraVen(request,id):
    suc=Venta.objects.get(id_venta=id)
    suc.delete()
    return redirect('Venta')