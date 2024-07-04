from django import forms
from apps.gestion.models import *




#this form will register the merchandiser
class register_merchandiser_Form(forms.ModelForm):

    class Meta:
        model = Mercancia
        fields=['trakin']




#this form will create the werehouse
class register_werehouse_Form(forms.ModelForm):
    class Meta:
        model = Wehrehouse
        fields=['tipo_persona' ,  'shipper' , 'recibido_de' , 'persona_recibe'  , 'peso_caja' ,'ancho_caja' , 'profundida_caja'  , 'pago' , 'regisro_cliente' 
                 , 'Tracking_num' ,  'contenido' , 'valor' ,   'comentarios' , 'onservaciones'] 


