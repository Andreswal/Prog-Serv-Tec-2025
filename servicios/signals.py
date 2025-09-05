# servicios/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Equipo, OrdenDeServicio

@receiver(post_save, sender=Equipo)
def create_orden_de_servicio(sender, instance, created, **kwargs):
    if created:
        OrdenDeServicio.objects.create(equipo=instance)