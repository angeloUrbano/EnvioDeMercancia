from django.urls import  path
from apps.gestion.views import *





urlpatterns =[
	path('home/',home.as_view(), name = 'index')
	]