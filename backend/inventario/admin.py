from django.contrib import admin

# Register your models here.
from .models import Producto, Existencia

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "precio")
    search_fields = ("nombre",)

@admin.register(Existencia)
class ExistenciaAdmin(admin.ModelAdmin):
    list_display = ("id", "producto", "cantidad_kg", "fecha_ingreso", "fecha_vencimiento")
    list_filter = ("fecha_ingreso",)