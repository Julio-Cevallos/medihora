from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Usuario, Medicamento, Recordatorio, Toma, Contacto
from .serializers import (
    UsuarioSerializer, MedicamentoSerializer, 
    RecordatorioSerializer, TomaSerializer, ContactoSerializer
)
from datetime import datetime, timedelta

class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    
    def get_queryset(self):
        return Usuario.objects.filter(cuenta=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(cuenta=self.request.user)


class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer


class RecordatorioViewSet(viewsets.ModelViewSet):
    serializer_class = RecordatorioSerializer
    
    def get_queryset(self):
        usuarios = Usuario.objects.filter(cuenta=self.request.user)
        return Recordatorio.objects.filter(usuario__in=usuarios, activo=True)
    
    @action(detail=False, methods=['get'])
    def proximos(self, request):
        """Obtener recordatorios ordenados por proximidad"""
        recordatorios = self.get_queryset().order_by('fecha_hora_inicio')
        serializer = self.get_serializer(recordatorios, many=True)
        return Response(serializer.data)


class TomaViewSet(viewsets.ModelViewSet):
    serializer_class = TomaSerializer
    
    def get_queryset(self):
        usuarios = Usuario.objects.filter(cuenta=self.request.user)
        recordatorios = Recordatorio.objects.filter(usuario__in=usuarios)
        return Toma.objects.filter(recordatorio__in=recordatorios)
    
    @action(detail=True, methods=['post'])
    def confirmar(self, request, pk=None):
        """Confirmar que se tomó el medicamento"""
        toma = self.get_object()
        toma.confirmado = True
        toma.save()
        return Response({'status': 'Toma confirmada'})


class ContactoViewSet(viewsets.ModelViewSet):
    serializer_class = ContactoSerializer
    
    def get_queryset(self):
        usuarios = Usuario.objects.filter(cuenta=self.request.user)
        return Contacto.objects.filter(usuario__in=usuarios)