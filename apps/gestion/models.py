from django.db import models
from apps.usuario.models import Usuario

class RegistroCliente(models.Model):
    nombre = models.CharField('Nombre del cliente',max_length = 150, blank= False, null=False)
    Apellido = models.CharField('Apellido del cliente',max_length = 150, blank= False, null=False)
    cedula = models.CharField('cedula del cliente',max_length = 150, blank= False, null=False)
    correo = models.EmailField(max_length=254, unique=True)
    correo_aux = models.EmailField(max_length=254, unique=True)
    telefono = models.CharField(max_length = 150)
    telefono_aux = models.CharField(max_length = 150)
    MY_CHOICES = (
        ('cliente1', 'Cliente Normal'),
        ('Cliente2', 'Ejecutivo'),
    )
    tipo_cliente = models.CharField(max_length=10, choices=MY_CHOICES)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre}, {self.Apellido}"


class Dirrecion(models.Model):
    direcion_estado = models.CharField(max_length = 150)
    direcion_municipio = models.CharField(max_length = 150)
    direcion_sector = models.CharField(max_length = 150)
    direcion_casa = models.CharField(max_length = 150)
    regisro_cliente = models.ForeignKey(RegistroCliente, verbose_name=("registro cliente"), on_delete=models.CASCADE)


class Mercancia(models.Model):
    wehrehouse_creado = models.BooleanField('Creacion', default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    regisro_cliente = models.ForeignKey(RegistroCliente, verbose_name=("registro cliente"), on_delete=models.CASCADE)
    trakin = models.IntegerField('codigo de paquete')

    def __str__(self):
        return f"Trakin: {self.trakin}"


class Wehrehouse(models.Model):
    MY_CHOICES = (
        ('Persona', 'Persona Natural'),
        ('Empresa', 'Persona Juridica'),
    )
    tipo_persona = models.CharField(max_length=60, choices=MY_CHOICES)
    shipper = models.CharField(max_length = 150, blank=True, null=False)
    recibido_de = models.CharField(max_length = 150)
    persona_recibe = models.CharField(max_length = 150)
    peso_caja = models.FloatField()
    ancho_caja = models.FloatField()
    profundida_caja = models.FloatField()
    pago = models.FloatField()
    regisro_cliente = models.ForeignKey(RegistroCliente, verbose_name=("registro cliente"), on_delete=models.CASCADE)
    Tracking_num  = models.IntegerField("")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    contenido = models.CharField(max_length = 150)
    valor = models.FloatField()
    comentarios = models.TextField()
    onservaciones= models.TextField()

    def __str__(self):
        return f"Trakin: {self.Tracking_num}"

    
    
    

    
    
    
    
    
    


    
    
