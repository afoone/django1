from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(length = 50)
    

    class Meta:
        verbose_name = _("Categoría")
        verbose_name_plural = _("Categorías")
        ordering = '-created'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})
