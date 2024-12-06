from django.urls import path
from provedor_app import views

urlpatterns = [
    path('Provedor',views.index_Provedor,name='Provedor'),
    path('regisProvedors/',views.regisProvedors,name='regisProvedors'),
    path('selecPro/<id>',views.selecPro,name="selecPro"),
    path('editPro/',views.editPro,name="editPro"),
    path('borraPro/<id>',views.borraPro,name="borraPro"),
]