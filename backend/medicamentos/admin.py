from django.contrib import admin
from .models import Usuario, Medicamento, Recordatorio, Toma, Contacto

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'cuenta', 'activo']
    list_filter = ['activo']

@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'dosis_predeterminada']
    search_fields = ['nombre']

@admin.register(Recordatorio)
class RecordatorioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'medicamento', 'fecha_hora_inicio', 'frecuencia_horas', 'activo']
    list_filter = ['activo', 'usuario']

@admin.register(Toma)
class TomaAdmin(admin.ModelAdmin):
    list_display = ['recordatorio', 'fecha_hora_toma', 'confirmado']
    list_filter = ['confirmado']

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'telefono', 'usuario']