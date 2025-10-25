from django.test import TestCase
from .models import Producto, Existencia
from django.db.utils import IntegrityError
from decimal import Decimal 
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

# Create your tests here.



class ProductoModelTest(TestCase):

    def setUp(self):
        self.producto = Producto.objects.create(
            nombre="Queso Semi Duro Bajo en Sal",
            descripcion="Queso artesanal con bajo contenido de sodio",
            precio=Decimal("12500.00")
        )

    def test_creacion_producto_exitosa(self):
        """ Verifica la creación exitosa de un producto con todos los campos válidos"""
        self.assertEqual(self.producto.nombre, "Queso Semi Duro Bajo en Sal")
        self.assertEqual(self.producto.precio, Decimal("12500.00"))
        self.assertIsInstance(self.producto, Producto)

    def test_precio_no_puede_ser_negativo(self):
        """ Verifica que no se pueda guardar un producto con precio negativo"""
        with self.assertRaises(ValidationError):
            Producto.objects.create(
                nombre="Queso Inválido",
                precio=-1000
            )

    def test_nombre_debe_ser_unico(self):
        with self.assertRaises(ValidationError):
            p = Producto(nombre="Queso Semi Duro Bajo en Sal", precio=18000)
            p.full_clean()  
            p.save()


class ExistenciaModelTest(TestCase):

    def setUp(self):
        self.producto = Producto.objects.create(
            nombre="Queso Costeño",
            precio=Decimal("9500.00")
        )
        self.existencia = Existencia.objects.create(
            producto=self.producto,
            cantidad_kg=Decimal("50.00")
        )

    def test_creacion_existencia_exitosa(self):
        """ Verifica que la existencia se crea correctamente"""
        self.assertEqual(self.existencia.producto.nombre, "Queso Costeño")
        self.assertEqual(self.existencia.cantidad_kg, Decimal("50.00"))

    def test_dependencia_producto(self):
        """ No se puede eliminar un producto si tiene existencias asociadas"""
        with self.assertRaises(Exception):
            self.producto.delete()
