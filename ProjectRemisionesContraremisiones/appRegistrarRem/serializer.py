from rest_framework import serializers
from .models import Afiliado, TipoIdentificacion, Parentesco,Profesional,Acompanante, Remision_Contraremision

class registrarRemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Afiliado
        fields = '__all__'

class TipoIdentificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoIdentificacion
        fields = '__all__'