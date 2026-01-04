#!/usr/bin/env bash
# exit on error
set -o errexit

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar migraciones
python manage.py migrate

# Recolectar archivos estáticos
python manage.py collectstatic --no-input

# Crear superusuario automáticamente
python manage.py create_superuser