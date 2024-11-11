from django.urls import  path
from apps.usuario.views import *




app_name='gestionurls'
urlpatterns =[
    
	path('login/',login.as_view(), name = 'login')
    
    ]