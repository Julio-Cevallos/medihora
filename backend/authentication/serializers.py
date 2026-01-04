from rest_framework import serializers
from .models import Cuenta

class RegistroSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = Cuenta
        fields = ['username', 'email', 'password']
    
    def create(self, validated_data):
        cuenta = Cuenta.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return cuenta


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = ['id', 'username', 'email', 'fecha_creacion']
        read_only_fields = ['id', 'fecha_creacion']