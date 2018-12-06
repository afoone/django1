from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length = 256, verbose_name="Título")
    pretitle = models.CharField(max_length = 128, verbose_name="Antetítulo", null=True, blank=True)
    description = models.TextField(verbose_name = "Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="services")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    urlfield = models.URLField(null=True, blank=True, max_length=200, verbose_name="Dirección Web")
    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ["-created"]

    def __str__(self):
        return self.title
