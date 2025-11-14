from django.contrib import admin
from .models import Companhia, Usuario, Servico, Localizacao, Problema

admin.site.register(Companhia)
admin.site.register(Usuario)
admin.site.register(Servico)
admin.site.register(Localizacao)
admin.site.register(Problema)
