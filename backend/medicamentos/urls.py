from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet, basename='usuario')
router.register(r'medicamentos', views.MedicamentoViewSet)
router.register(r'recordatorios', views.RecordatorioViewSet, basename='recordatorio')
router.register(r'tomas', views.TomaViewSet, basename='toma')
router.register(r'contactos', views.ContactoViewSet, basename='contacto')

urlpatterns = [
    path('', include(router.urls)),
]