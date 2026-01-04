from django.db import models
from authentication.models import Cuenta

class Usuario(models.Model):
    """Perfil de persona mayor asociada a una cuenta"""
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE, related_name='usuarios')
    nombre = models.CharField(max_length=100)
    foto_perfil = models.ImageField(upload_to='perfiles/', null=True, blank=True)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'usuarios'


class Medicamento(models.Model):
    """Catálogo de medicamentos disponibles"""
    nombre = models.CharField(max_length=100)
    dosis_predeterminada = models.CharField(max_length=50)
    nota_general = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.nombre} - {self.dosis_predeterminada}"
    
    class Meta:
        db_table = 'medicamentos'


class Recordatorio(models.Model):
    """Horarios programados para tomar medicamentos"""
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='recordatorios')
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    fecha_hora_inicio = models.DateTimeField()
    frecuencia_horas = models.IntegerField(help_text="Frecuencia en horas")
    nota_especifica = models.TextField(blank=True)
    activo = models.BooleanField(default=True)
    notification_ids = models.JSONField(default=list, blank=True) 
    
    def __str__(self):
        return f"{self.usuario.nombre} - {self.medicamento.nombre}"
    
    class Meta:
        db_table = 'recordatorios'
        ordering = ['fecha_hora_inicio']


class Toma(models.Model):
    """Registro de tomas de medicamentos (confirmadas o no)"""
    recordatorio = models.ForeignKey(Recordatorio, on_delete=models.CASCADE, related_name='tomas')
    fecha_hora_toma = models.DateTimeField()
    confirmado = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.recordatorio} - {self.fecha_hora_toma}"
    
    class Meta:
        db_table = 'tomas'
        ordering = ['fecha_hora_toma']


class Contacto(models.Model):
    """Contactos de emergencia"""
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='contactos')
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombre} - {self.usuario.nombre}"
    
    class Meta:
        db_table = 'contactos'