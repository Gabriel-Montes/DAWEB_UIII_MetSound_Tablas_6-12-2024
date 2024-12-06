from django.shortcuts import render,redirect
from .models import Empleado

# Create your views here.
def index_Empleados(request):
    nEmpleados=Empleado.objects.all()
    return render(request,'gestEmp.html',{'lamp':nEmpleados})

def regisEmpleados(request): 
    id=request.POST["txtid"]
    nombre=request.POST["txtnom"]
    pues=request.POST["pue"]
    dire=request.POST["dir"]
    suel=request.POST["sue"]
    edad=request.POST["edad"]
    cel=request.POST["cel"]
    
    guarEmpleado=Empleado.objects.create(
            id_emple=id,
            nombre=nombre,
            puesto=pues,
            direccion=dire,
            sueldo=suel,
            edad=edad,
            celular=cel
    )
    return redirect("Empleados")

def selecEmp(request,id):
    cli=Empleado.objects.get(id_emple=id)
    return render(request,'editarEmp.html',{"mEmpleados":cli})

def editEmp(request):
    id=request.POST["txtid"]
    nombre=request.POST["txtnom"]
    pues=request.POST["pue"]
    dire=request.POST["dir"]
    suel=request.POST["sue"]
    edad=request.POST["edad"]
    cel=request.POST["cel"]
    emp=Empleado.objects.get(id_emple=id)
    emp.nombre=nombre
    emp.puesto=pues
    emp.direccion=dire
    emp.sueldo=suel
    emp.edad=edad
    emp.celular=cel
    emp.save()
    return redirect('Empleados')

def borraEmp(request,id):
    cli=Empleado.objects.get(id_emple=id)
    cli.delete()
    return redirect('Empleados')