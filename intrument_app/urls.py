from django.urls import path
from intrument_app import views

urlpatterns = [
    path('Instrumento',views.index_Instruments,name='Instrumento'),
    path('regisInstruments/',views.regisInstruments,name='regisInstruments'),
    path('selecins/<id>',views.selecins,name="selecins"),
    path('editIns/',views.editIns,name="editIns"),
    path('borraIns/<id>',views.borraIns,name="borraIns"),
]