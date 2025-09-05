from django.contrib import admin
from .models import Cliente, TipoEquipo, Marca, Modelo, Equipo, OrdenDeServicio

# Personaliza la vista del modelo Cliente
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'telefono', 'correo')
    search_fields = ('nombre', 'apellido', 'telefono')
    list_filter = ('ciudad',)

# Personaliza la vista del modelo TipoEquipo
@admin.register(TipoEquipo)
class TipoEquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

# Personaliza la vista del modelo Marca
@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

# Personaliza la vista del modelo Modelo
@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca')
    search_fields = ('nombre', 'marca__nombre')
    list_filter = ('marca',)

# Personaliza la vista del modelo Equipo
@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'tipo_equipo', 'marca', 'modelo', 'falla_declarada')
    search_fields = ('cliente__nombre', 'cliente__apellido', 'tipo_equipo__nombre', 'marca__nombre', 'modelo__nombre')
    list_filter = ('tipo_equipo', 'marca')
    list_per_page = 25
    raw_id_fields = ('cliente',)
    autocomplete_fields = ['tipo_equipo', 'marca', 'modelo']
    
# Registra el modelo de la Orden de Servicio sin personalización por ahora
admin.site.register(OrdenDeServicio)