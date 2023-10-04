from django.db import models

class Paleta(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha_lanzamiento = models.DateField()
    
    def __str__(self):
        return f'{self.marca} {self.modelo}'
    