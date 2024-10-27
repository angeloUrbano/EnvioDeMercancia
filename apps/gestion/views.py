import json
from typing import Any

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic import ListView , CreateView , UpdateView , DeleteView , DetailView ,TemplateView
from django.http import JsonResponse

from apps.gestion.models import Mercancia , RegistroCliente , Wehrehouse , Carrito
from apps.gestion.forms import register_merchandiser_Form , register_werehouse_Form
from apps.usuario.models import  Usuario
from django.core.exceptions import ObjectDoesNotExist


from django.shortcuts import render, redirect, get_object_or_404

class home(TemplateView):
    template_name = 'index.html'


#this class will create the merchandiseregister  than arrive to the company 



# **********************NOTA : THE CLIENT REGISTER AND MERCHANDISE REGISTER MUST BE DONE AT SAME TIME*********************************

class create_merchandise(CreateView):
    model = Mercancia
    #fields = '__all__'
    template_name = 'gestion/merchandise_register.html'
    form_class = register_merchandiser_Form

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if not  request.ajax_request:
            return redirect("gestionurls:registro_cliente")

    


    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:

        data  =json.loads(request.body)
        if request.ajax_request:
            if data :
                object_to_save = self.model()
                object_to_save.usuario_id = request.user.id 
                object_to_save.trakin = data['merchandise']   
                object_to_save.regisro_cliente = RegistroCliente.objects.get(id=data['id'])
                object_to_save.save()  

                return JsonResponse({"success": "Se registro la mercancia"})
            else:
                return JsonResponse({"error":"No se registro la mercancia"})
        
        return redirect("gestionurls:buscarcliente")

def agregar_a_carrito(request, wherehouse_id):
    wherehouse = get_object_or_404(Wehrehouse, id=wherehouse_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    carrito.wherehouses.add(wherehouse)
    return redirect('gestionurls:mostrar_carrito')


def mostrar_carrito(request):
    carrito = Carrito.objects.filter(usuario=request.user).first()
    return render(request, 'gestion/carrito.html', {'carrito': carrito})




#this class create a werehouse
class create_warehouse(CreateView):
    model = Wehrehouse
    template_name = "gestion/create_warehouse_template.html"
    form_class = register_werehouse_Form



    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:


        carrito = Carrito.objects.filter(usuario=request.user).first()

        return render(self.request , self.template_name , {"form":self.form_class ,  'carrito': carrito})
    

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:

        if request.ajax_request:
            # Access form data directly 
            warehouse = request.POST.copy()  # Replace 'warehouse_name' with your actual field name
            # Convertir listas a valores simples
            new = {}
            warehouse.pop('alto' , None)
            for key in warehouse.keys():
                # Verificar si el valor es una lista y tomar el primer elemento
                new[key] = warehouse[key]
            
            new['usuario_id']=request.user.id
            new['peso_caja']=1111
            new['pago']=1111
            new['regisro_cliente_id']=request.user.id

            object_to_create = self.model(**new)
            object_to_create.save()
            nuevo_id = object_to_create.id

            
            wherehouse = get_object_or_404(Wehrehouse, id=nuevo_id)
            carrito, created = Carrito.objects.get_or_create(usuario=request.user)
            carrito.wherehouses.add(wherehouse)

            # Process the data as needed
            return JsonResponse({'success': True, 'message': 'Warehouse created successfully!'})
        return JsonResponse({'error': 'Invalid request'}, status=400)

        # form = self.form_class(request.POST)
        # if form.is_valid():

        #     print("it is ok")
        #     data = form.cleaned_data
        #     data['usuario_id']=request.user.id
        #     object_to_create = self.model(**data)
        #     object_to_create.save()

        #     nuevo_id = object_to_create.id

        #     wherehouse = get_object_or_404(Wehrehouse, id=nuevo_id)
        #     carrito, created = Carrito.objects.get_or_create(usuario=request.user)
        #     carrito.wherehouses.add(wherehouse)

            
            #return redirect('gestionurls:creating_warehouseName')

        # else:
        #     print("it is not ok")    

        # return super().post(request, *args, **kwargs)
    


def delete_wherehouse(request, wherehouse_id):

    if request.method == 'DELETE':
        print("entro en el delete")
        wherehouse = get_object_or_404(Wehrehouse, id=wherehouse_id)
        wherehouse.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

#this class will show each warehouse previously created
class show_werehouse(ListView):
    model= Wehrehouse 
    template_name =  "gestion/show_werehose_templete.html"



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
                'id': cliente.id,
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


   




    

