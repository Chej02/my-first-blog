from django.contrib import admin
from PROYECTO_APP.models import Material, MaterialAdmin, Encabezado, EncabezadoAdmin
# Register your models here.
admin.site.register(Material, MaterialAdmin)
admin.site.register(Encabezado, EncabezadoAdmin)
