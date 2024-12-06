from django.urls import path
from empleados_app import views

urlpatterns = [
    path('Empleados',views.index_Empleados,name='Empleados'),
    path('regisEmpleados/',views.regisEmpleados,name='regisEmpleados'),
    path('selecEmp/<id>',views.selecEmp,name="selecEmp"),
    path('editEmp/',views.editEmp,name="editEmp"),
    path('borraEmp/<id>',views.borraEmp,name="borraEmp"),
]