from django.contrib import admin
from apps.usuario.models import Usuario
from apps.gestion.models import RegistroCliente, Dirrecion, Mercancia, Wehrehouse

admin.site.register(Usuario)
admin.site.register(RegistroCliente)
admin.site.register(Dirrecion)
admin.site.register(Mercancia)
admin.site.register(Wehrehouse)
