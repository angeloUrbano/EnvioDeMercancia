import os
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
from django.urls import reverse



from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle

class home(TemplateView):
    template_name = 'index.html'
    


#this class will create the merchandiseregister  than arrive to the company 





class pdfReport(ListView):

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:



        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        pdf_path = os.path.join(downloads_path, "warehouse_receipt_report.pdf")

        # Create the PDF canvas
        c = canvas.Canvas(pdf_path, pagesize=A4)
        width, height = A4

        # Header Section
        c.setFont("Helvetica-Bold", 12)
        c.drawString(30, height - 40, "ENEX VENEZUELA")
        c.setFont("Helvetica", 10)
        c.drawString(30, height - 60, "8534 NW 66TH ST MIAMI FL 33166")
        c.drawString(30, height - 75, "Phone: (786) 2122423 / (786) 2122423 / Fax: (0)")
        c.drawString(30, height - 90, "operaciones@taymarcargo.com")

        # Warehouse Receipt Details
        c.setFont("Helvetica-Bold", 12)
        c.drawString(400, height - 40, "WareHouse Receipt #:")
        c.setFont("Helvetica-Bold", 18)
        c.drawString(500, height - 40, "246217")

        c.setFont("Helvetica", 8)
        c.drawString(400, height - 55, "Printed Date: 3/12/2024-2:19:56 PM | Received By: 3/12/2024 1:07:26 PM")

        # Shipper and Consignee Information
        c.setFont("Helvetica-Bold", 10)
        c.drawString(30, height - 120, "Shipper Information")
        c.drawString(300, height - 120, "Consignee Information")
        c.setFont("Helvetica", 8)
        c.drawString(30, height - 135, "8534 NW 66TH ST MIAMI FL 33166, MIAMI")
        c.drawString(300, height - 135, "MARIO ZAMBRANO")
        c.drawString(300, height - 150, "VALENCIA CARABOBO VENEZUELA")
        c.drawString(300, height - 165, "VALENCIA, VENEZUELA")

        # Office Destination and Payment Type Information
        c.setFont("Helvetica-Bold", 10)
        c.drawString(300, height - 190, "Oficina Destino: TITANIUM VALENCIA")
        c.setFont("Helvetica", 8)
        c.drawString(30, height - 190, "Payment Type | Shipment Type | # Casillero")
        c.drawString(30, height - 205, "COD | POR DEFINIR | # 117")

        # Draw a line to separate sections
        c.line(30, height - 215, width - 30, height - 215)

        # Package Details Table
        data = [
            ["Line/Qty", "Dimensions (In)", "Tracking", "Weight lb", "Vol lb", "Weight Ft3", "Vol Ft3", "Weight Kg"],
            ["1/1", "19x7x15 BOX", "TBA312078550473", "5.00", "12.02", "0.48", "1.15", "2.2"],
            ["2/1", "16x7x13 BOX", "TBA312077156361", "4.00", "8.77", "0.38", "0.84", "1.8"],
            ["3/1", "14x6x11 BOX", "TBA312078028394", "3.00", "5.57", "0.29", "0.53", "1.3"],
            ["4/1", "13x8x11 BOX", "TBA312079683675", "3.00", "6.89", "0.29", "0.66", "1.3"],
            ["Pzas: 4", "", "", "15.00", "33.25", "1.44", "3.19", "6.6"]
        ]

        table = Table(data, colWidths=[0.75 * inch, 1.5 * inch, 1.5 * inch, 0.75 * inch, 0.75 * inch, 0.75 * inch, 0.75 * inch, 0.75 * inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 8),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ]))

        # Position table on the PDF
        table.wrapOn(c, width, height)
        table.drawOn(c, 30, height - 400)

        # Note and Footer
        c.drawString(30, height - 420, "Entregado por: AMAZON")
        c.drawString(300, height - 420, "Nombre Completo")
        c.drawString(450, height - 420, "Fecha y Hora")

        # Footer Note
        footer_text = """
        NOTA: SE ESTA ENTREGANDO ESTA CAJA COMPLETAMENTE SELLADA.
        Certifico que este envío no contiene dinero, narcóticos, armas o dispositivos explosivos no autorizados. TITANIUM INTERNATIONAL INC no se hace
        responsable de los artículos no retirados en los treinta (30) días siguientes a su recepción. Nuestra responsabilidad en caso de siniestros durante
        el transporte aéreo o marítimo, extravío o robos será de $100 dólares por recibo de almacén, si el cliente no asegura la carga. Estoy de acuerdo
        con que este envío esté sujeto a los controles de seguridad de la compañía y otras regulaciones gubernamentales."""

        text = c.beginText(30, height - 470)
        text.setFont("Helvetica", 6)
        text.setLeading(8)
        text.textLines(footer_text)
        c.drawText(text)

        # Save the PDF
        c.save()
        pdf_path


        return super().get(request, *args, **kwargs)



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
            carrito = Carrito.objects.filter(usuario=request.user).first()

              # Check if carrito exists to avoid AttributeError
            if carrito:
                # Prepare the carrito data
                carrito_data = {
                    'id': carrito.id,
                    'usuario_id': carrito.usuario.id,  # User ID
                    'fecha_creacion': carrito.fecha_creacion.isoformat(),  # Format date as ISO string
                    'wherehouses': []
                }

                # Iterate through wherehouses to add delete URLs
                for wherehouse in carrito.wherehouses.all():  # Assuming you want to iterate through related wherehouses
                    carrito_data['wherehouses'].append({
                        'id': wherehouse.id,
                        'tipo_persona': wherehouse.tipo_persona,
                        'Tracking_num': wherehouse.Tracking_num,
                        'contenido': wherehouse.contenido,
                        'deleteUrl': reverse('gestionurls:delete_wherehouse', kwargs={'wherehouse_id': wherehouse.id})  # Generate delete URL
                    })
            else:
                carrito_data = {}




            return JsonResponse({'success': True, 'message': 'Warehouse created successfully!', 'carrito': carrito_data})

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


   




    

