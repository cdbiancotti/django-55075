from django.db import models


class Curso(models.Model):
    titulo = models.CharField(max_length=50)
    numero = models.IntegerField()
    
    def __str__(self):
        return f'{self.titulo} {self.numero}'