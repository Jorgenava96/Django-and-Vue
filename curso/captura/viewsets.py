from rest_framework import viewsets
from .models import Expediente
from .serializer import ExpedienteSerializer

class ExpedienteViewSet(viewsets.ModelViewSet):
    queryset = Expediente.objects.all()
    serializer_class = ExpedienteSerializer