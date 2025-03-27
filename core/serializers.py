from rest_framework import serializers
from .models import ProyectoInmobiliario, UnidadPropiedad, Cliente

class UnidadPropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadPropiedad
        fields = '__all__'

class ProyectoSerializer(serializers.ModelSerializer):
    unidades = UnidadPropiedadSerializer(many=True, read_only=True)
    class Meta:
        model = ProyectoInmobiliario
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
