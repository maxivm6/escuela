from django.db import models
from colorfield.fields import ColorField


# Create your models here.
class Seccion(models.Model):
    titulo = models.TextField(max_length=50)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='blog',null=True,blank=True)
    color_fondo = ColorField(format="hexa")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='seccion'
        verbose_name_plural='secciones' 
    
   