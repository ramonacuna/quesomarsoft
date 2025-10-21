from django.db import models
from django.core.validators import MinValueValidator 

# Create your models here.
class Producto(models.Model):
    """
    Representa un producto del catálogo general.
    En este caso, los distintos tipos de quesos u otros productos elaborados o vendidos.
    """
    nombre = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Nombre del producto"
    )
    descripcion = models.TextField(
        blank=True,
        null=True,
        verbose_name="Descripción"
    )
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        default=0,
        verbose_name="Precio por kg (COP)",
        null=False,       # 🔒 No puede ser nulo en la base de datos
        blank=False       # 🔒 No puede quedar vacío en formularios
    )   

    class Meta:
        db_table = "inventario_producto"
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Existencia(models.Model):
    """
    Representa el registro de lotes de productos existentes en inventario.
    Cada registro pertenece a un producto y contiene detalles específicos del lote.
    """
    producto = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT,
        related_name="lotes",
        verbose_name="Producto asociado"
    )
    lote = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Código de lote"
    )
    proveedor = models.CharField(
        max_length=100,
        verbose_name="Proveedor"
    )
    cantidad_kg = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Cantidad (kg)"
    )
    fecha_ingreso = models.DateField(
        verbose_name="Fecha de ingreso"
    )
    fecha_vencimiento = models.DateField(
        verbose_name="Fecha de vencimiento"
    )

    class Meta:
        db_table = "inventario_existencia"
        verbose_name = "Existencia"
        verbose_name_plural = "Existencias"
        ordering = ["-fecha_ingreso"]

    def __str__(self):
        return f"{self.producto.nombre} - Lote {self.lote}"

    def esta_vencido(self):
        """
        Método auxiliar para verificar si un lote está vencido.
        """
        from datetime import date
        return date.today() > self.fecha_vencimiento