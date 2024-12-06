from django.shortcuts import render,redirect
from .models import Instrument

# Create your views here.
def index_Instruments(request):
    nInstruments=Instrument.objects.all()
    return render(request,'gestIns.html',{'mInstruments':nInstruments})

def regisInstruments(request): 
    id=request.POST["txtid"]
    marca=request.POST["txtmar"]
    tama=request.POST["tam"]
    esta=request.POST["est"]
    lugar=request.POST["lugar"]
    fec=request.POST["fecha"]
    ven=request.POST["vend"]
    
    guarInstrument=Instrument.objects.create(
            id_instru=id,
            marca=marca,
            tamano=tama,
            estado=esta,
            lugar=lugar,
            mantenimiento=fec,
            vendido=ven
    )
    return redirect("Instrumento")

def selecins(request,id):
    cli=Instrument.objects.get(id_instru=id)
    return render(request,'editarIns.html',{"mInstruments":cli})

def editIns(request):
    id=request.POST["txtid"]
    marca=request.POST["txtmar"]
    tama=request.POST["tam"]
    esta=request.POST["est"]
    lugar=request.POST["lugar"]
    fec=request.POST["fecha"]
    ven=request.POST["vend"]
    ins=Instrument.objects.get(id_instru=id)
    ins.marca=marca
    ins.tamano=tama
    ins.estado=esta
    ins.lugar=lugar
    ins.mantenimiento=fec
    ins.vendido=ven
    ins.save()
    return redirect('Instrumento')

def borraIns(request,id):
    cli=Instrument.objects.get(id_instru=id)
    cli.delete()
    return redirect('Instrumento')