from rest_framework import viewsets
from .models import Afiliado, TipoIdentificacion
from .serializer import registrarRemSerializer, TipoIdentificacionSerializer


class AfiliadoViewSet(viewsets.ModelViewSet):
    queryset = Afiliado.objects.all()
    serializer_class = registrarRemSerializer


class TipoIdenficacionViewSet(viewsets.ModelViewSet):
    queryset = TipoIdentificacion.objects.all()
    serializer_class = TipoIdentificacionSerializer
