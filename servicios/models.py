# servicios/models.py

from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(blank=True, null=True)
    domicilio = models.CharField(max_length=200, blank=True)
    ciudad = models.CharField(max_length=100, blank=True)
    provincia = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class TipoEquipo(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre
    
class Marca(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.nombre

# servicios/models.py

class Modelo(models.Model):
    nombre = models.CharField(max_length=50, unique=True) # Agregamos unique=True
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.marca.nombre} {self.nombre}"
    

class Equipo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo_equipo = models.ForeignKey(TipoEquipo, on_delete=models.SET_NULL, null=True)
    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.SET_NULL, null=True)
    imei = models.CharField(max_length=20, blank=True, null=True)
    serie = models.CharField(max_length=50, blank=True, null=True)
    accesorios = models.TextField(blank=True)
    falla_declarada = models.TextField()

    def __str__(self):
        # Corrección: Acceder al nombre del tipo de equipo
        return f"{self.tipo_equipo.nombre} {self.marca} {self.modelo} - Cliente: {self.cliente.nombre}"


class OrdenDeServicio(models.Model):
    ESTADO_CHOICES = (
        ('ingresado', 'Equipo Ingresado'),
        ('revisado', 'Revisado'),
        ('presupuestado', 'Presupuestado'),
        ('espera_repuesto', 'En Espera de Repuesto'),
        ('reparado', 'Reparado'),
        ('no_reparable', 'No Reparable'),
        ('presupuesto_aceptado', 'Presupuesto Aceptado'),
        ('entregado', 'Entregado'),
    )

    equipo = models.OneToOneField(Equipo, on_delete=models.CASCADE)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES, default='ingresado')
    informe = models.TextField(blank=True, verbose_name="Informe Técnico")
    
    # Campos para la garantía
    es_garantia = models.BooleanField(default=False)
    fecha_compra_garantia = models.DateField(blank=True, null=True)
    numero_factura_garantia = models.CharField(max_length=50, blank=True, null=True)
    orden_marca_garantia = models.CharField(max_length=50, blank=True, null=True)
    
    # Campos para el presupuesto (cuando no es garantía)
    presupuesto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    # Campo para registrar la fecha de entrega
    fecha_entrega = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Orden N°{self.pk} - {self.equipo.marca} {self.equipo.modelo}"
