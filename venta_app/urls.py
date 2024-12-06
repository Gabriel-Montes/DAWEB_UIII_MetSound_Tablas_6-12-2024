from django.urls import path
from venta_app import views

urlpatterns = [
    path('Venta',views.index_Venta,name='Venta'),
    path('regisVentas/',views.regisVentas,name='regisVentas'),
    path('selecVen/<id>',views.selecVen,name="selecVen"),
    path('editVen/',views.editVen,name="editVen"),
    path('borraVen/<id>',views.borraVen,name="borraVen"),
]