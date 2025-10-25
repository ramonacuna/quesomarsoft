from django.shortcuts import render


# Create your views here.
from rest_framework import viewsets
from .models import Producto,Existencia
from .serializers import ProductoSerializer,ExistenciaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ExistenciaViewSet(viewsets.ModelViewSet):
    queryset = Existencia.objects.select_related("producto").all()
    serializer_class = ExistenciaSerializer