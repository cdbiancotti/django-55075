from django.db import models


class Curso(models.Model):
    titulo = models.CharField(max_length=50)
    numero = models.IntegerField()