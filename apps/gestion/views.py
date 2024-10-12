from typing import Any

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic import ListView , CreateView , UpdateView , DeleteView , DetailView ,TemplateView
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes

from apps.gestion.models import Mercancia , RegistroCliente , Wehrehouse
from apps.gestion.forms import register_merchandiser_Form , register_werehouse_Form
from apps.usuario.models import  Usuario
from django.core.exceptions import ObjectDoesNotExist


class home(TemplateView):
    template_name = 'index.html'


#this class will create the merchandiseregister  than arrive to the company 



# **********************NOTA : THE CLIENT REGISTER AND MERCHANDISE REGISTER MUST BE DONE AT SAME TIME*********************************

class create_merchandise(CreateView):
    model = Mercancia
    #fields = '__all__'
    template_name = 'gestion/merchandise_register.html'
    form_class = register_merchandiser_Form

    #success_url = '/merchandise_register'



    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        return render(self.request , self.template_name , {"form":self.form_class})
    


    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:

        print("pasada por el post con su informacio")

        
        form = self.form_class(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            print(info)
            user  = request.user.id 
            object_to_save = self.model()
            object_to_save.usuario_id = request.user.id 
            object_to_save.trakin = info['trakin']   
            object_to_save.regisro_cliente = RegistroCliente.objects.latest('id') # i should do better, 
            object_to_save.save()   

            print("it is valid" , user)
            return redirect('gestionurls:merchandiser_registerName')
        else:
            return render(self.request , self.template_name , {"form":form})
        



#this class create a werehouse
class create_warehouse(CreateView):
    model = Wehrehouse
    template_name = "gestion/create_warehouse_template.html"
    form_class = register_werehouse_Form



    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        return render(self.request , self.template_name , {"form":self.form_class})
    

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:

        form = self.form_class(request.POST)
        if form.is_valid():

            print("it is ok")
            data = form.cleaned_data
            data['usuario_id']=request.user.id
            object_to_create = self.model(**data)
            object_to_create.save()
            return redirect('gestionurls:merchandiser_registerName')

        else:
            print("it is not ok")    

        return super().post(request, *args, **kwargs)
    



#this class will show each warehouse previously created
class show_werehouse(ListView):
    model= Wehrehouse 
    template_name =  "gestion/show_werehose_templete.html"

<<<<<<< Updated upstream
=======


#vista de registro del clientes

class RegistroClientes(TemplateView):
    template_name = "gestion/registro_cliente.html"

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:            
        #  usuario  por defecto(cambiar)
        usuario = Usuario.objects.get(id=1) 
        #  objeto RegistroCliente
        registro_cliente = RegistroCliente(
        nombre=request.POST.get('nombre'),
        Apellido=request.POST.get('apellido'),
        cedula=request.POST.get('cedula'),
        correo=request.POST.get('correo'),
        correo_aux=request.POST.get('correo_axi'),
        telefono=request.POST.get('telefono'),
        telefono_aux=request.POST.get('telefono_axi'),
        tipo_cliente='cliente1', # esta por defecto (falta registro cliente Ejecutivo)
        usuario=usuario
    )
        registro_cliente.save() #guardado
         # diccionario con los datos del registro_cliente
        datos_registro_cliente = {
            'id': registro_cliente.id,
            'nombre': registro_cliente.nombre,
            'apellido': registro_cliente.Apellido,
            'cedula': registro_cliente.cedula,
            'correo': registro_cliente.correo,
            'correo_aux': registro_cliente.correo_aux,
            'telefono': registro_cliente.telefono,
            'telefono_aux': registro_cliente.telefono_aux,
            'tipo_cliente': registro_cliente.tipo_cliente,
            'usuario': registro_cliente.usuario.username
        }
        #   delvorver dicionario y mensaje

        print("proceso de registrar usuario..............   ")
        return JsonResponse({'mensaje': 'Cliente registrado con éxito', 'datos': datos_registro_cliente})

       



# funcion  de buscar cliente en la vista 
@require_http_methods(['POST'])
def buscar_cliente(request):
    if request.ajax_request:  #request.ajax_request en lugar de request.is_ajax()
        q = request.POST.get('q')
        try:
            cliente = RegistroCliente.objects.get(cedula=q)
            mensaje = "El Cliente Existe"
            datos_cliente = {
                'nombre': cliente.nombre,
                'cedula': cliente.cedula,
                'correo': cliente.correo,
                'telefono': cliente.telefono
            }
        except ObjectDoesNotExist:
            mensaje = 'El Cliente no Existe'
            datos_cliente = {}
        return JsonResponse({'mensaje': mensaje, 'datos_cliente': datos_cliente})
    else:
        return HttpResponseBadRequest('Solicitud no válida')


   




    

>>>>>>> Stashed changes
