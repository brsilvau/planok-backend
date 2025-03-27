from rest_framework import viewsets, filters
from drf_spectacular.utils import extend_schema
from .models import ProyectoInmobiliario, UnidadPropiedad, Cliente
from .serializers import (
    ProyectoSerializer,
    UnidadPropiedadSerializer,
    ClienteSerializer
)

@extend_schema(tags=['Proyectos'])
class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = ProyectoInmobiliario.objects.all()
    serializer_class = ProyectoSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'ubicacion', 'descripcion']
    ordering_fields = ['fecha_creacion', 'nombre']

@extend_schema(tags=['Unidades'])
class UnidadPropiedadViewSet(viewsets.ModelViewSet):
    queryset = UnidadPropiedad.objects.all()
    serializer_class = UnidadPropiedadSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['numero_unidad', 'tipo_unidad', 'estado']
    ordering_fields = ['fecha_creacion', 'precio_venta']

@extend_schema(tags=['Clientes'])
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['rut', 'nombre', 'apellido', 'correo_electronico']
    ordering_fields = ['fecha_creacion', 'nombre']
