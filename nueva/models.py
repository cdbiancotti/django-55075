from django.db import models
from ckeditor.fields import RichTextField

class Paleta(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    descripcion = RichTextField()
    fecha_lanzamiento = models.DateField()
    
    def __str__(self):
        return f'{self.marca} {self.modelo}'
    