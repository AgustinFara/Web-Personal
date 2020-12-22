from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Título")
    description = models.TextField(verbose_name = "Descripción")
    image = models.ImageField(verbose_name = "Imagen", upload_to = 'projects')
    date = models.DateField(verbose_name = "Fecha")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Cronomarcador de creación")
    updated = models.DateTimeField(auto_now =True, verbose_name = "Cronomarcador de modificación")
    link = models.URLField(blank=True, null=True, verbose_name = "link para más información")

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-date']

    def __str__(self):
        return self.title
