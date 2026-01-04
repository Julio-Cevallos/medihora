from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cuenta

@admin.register(Cuenta)
class CuentaAdmin(UserAdmin):
    list_display = ['username', 'email', 'fecha_creacion']
    fieldsets = UserAdmin.fieldsets + (
        ('Información adicional', {'fields': ('fecha_creacion',)}),
    )
    readonly_fields = ['fecha_creacion']