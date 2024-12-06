from django.urls import path
from sucursal_app import views

urlpatterns = [
    path('Sucursal',views.index_Sucursal,name='Sucursal'),
    path('regisSucursals/',views.regisSucursals,name='regisSucursals'),
    path('selecSuc/<id>',views.selecSuc,name="selecSuc"),
    path('editSuc/',views.editSuc,name="editSuc"),
    path('borraSuc/<id>',views.borraSuc,name="borraSuc"),
]