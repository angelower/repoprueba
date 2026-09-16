# Gestión de Pacientes

Proyecto de práctica (práctica 1) del curso Ingeniería de Software — Bioingeniería, Universidad de Antioquia. Aplicación web base construida con Django para la gestión de pacientes.

## Stack

- Python / Django 6.1.1
- SQLite (`db.sqlite3`)

## Estructura

```
gestion_pacientes/   # Configuración del proyecto Django (settings, urls, wsgi/asgi)
pacientes/           # App de Django: modelos, vistas, urls, templates para gestión de pacientes.
devices/             # App de Django: modelos, vistas, urls, templates para gestión de equipo biomédicos. equipo, marca, serial
manage.py            # CLI de administración de Django
requirements.txt     # Dependencias del proyecto
```

Rutas actuales:
- `/admin/` — panel de administración de Django.
- `/pacientes/` — vista índice de la app `pacientes`.

## Instalación

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Uso

```bash
python manage.py migrate
python manage.py runserver
```

La aplicación queda disponible en `http://127.0.0.1:8000/`.

## Estado

Proyecto en etapa inicial: la app `pacientes` aún no define modelos ni lógica de negocio; solo cuenta con una vista índice de ejemplo.
