from rest_framework import serializers
from .models import Usuario, Medicamento, Recordatorio, Toma, Contacto

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        read_only_fields = ['cuenta']


class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '__all__'


class RecordatorioSerializer(serializers.ModelSerializer):
    medicamento_nombre = serializers.CharField(source='medicamento.nombre', read_only=True)
    medicamento_dosis = serializers.CharField(source='medicamento.dosis_predeterminada', read_only=True)
    usuario_nombre = serializers.CharField(source='usuario.nombre', read_only=True)
    
    class Meta:
        model = Recordatorio
        fields = '__all__'


class TomaSerializer(serializers.ModelSerializer):
    recordatorio_info = RecordatorioSerializer(source='recordatorio', read_only=True)
    
    class Meta:
        model = Toma
        fields = '__all__'


class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = '__all__'