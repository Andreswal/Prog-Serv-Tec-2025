from django.contrib import admin
from .models import Cliente, Equipo, OrdenDeServicio

# Registra tus modelos aquí.
admin.site.register(Cliente)
admin.site.register(Equipo)
admin.site.register(OrdenDeServicio)