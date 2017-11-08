from django.db import models
from django.contrib import admin
#ACTOR = MATERIAL
#PELICULA = ENCABEZADO
#ACTUACION = DESCRIPCION
class Material(models.Model):
    nombre = models.CharField(max_length=100)
    unidad = models.CharField(max_length=30)
    precio = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre
class Encabezado(models.Model):
    fecha = models.DateField()
    encargado = models.CharField(max_length=60)
    materiales = models.ManyToManyField(Material, through='Descripcion')
    def __str__(self):
        return self.encargado

class Descripcion (models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    encabezado = models.ForeignKey(Encabezado, on_delete=models.CASCADE)


class DescripcionInLine(admin.TabularInline):
    model = Descripcion
    extra = 1

class MaterialAdmin(admin.ModelAdmin):
    inlines = (DescripcionInLine,)

class EncabezadoAdmin (admin.ModelAdmin):
    inlines = (DescripcionInLine,)
