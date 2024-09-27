from django.urls import  path
from apps.gestion.views import *




app_name='gestionurls'
urlpatterns =[
	path('home/',home.as_view(), name = 'index'),

	#Gestion
    
	#path to create merchandise
	path('merchandiser_register/' , create_merchandise.as_view() , name='merchandiser_registerName'),
    

	#path to create werehouse
    path('creating_warehouse/' , create_warehouse.as_view() , name='creating_warehouseName'),
    
	
    #path to show werehouse created
	path('showing_warehouse/' , show_werehouse.as_view() , name='showing_warehouseName'),

    path("registro_cliente/", RegistroCliente.as_view(), name="registro cliente")
    
]