from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length = 256, verbose_name="Título")
    content = models.TextField(verbose_name = "Contenido")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Page_detail", kwargs={"pk": self.pk})

