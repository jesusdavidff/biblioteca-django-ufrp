# Biblioteca Django App

Este directorio contiene la aplicación Django `biblioteca` para el proyecto.

## Cómo ejecutar localmente

1. Asegúrate de estar en el directorio del proyecto:
   ```powershell
   cd c:\Users\Daniel\OneDrive\Documents\ejercicio_django
   ```

2. Activa el entorno virtual:
   ```powershell
   .\venv\Scripts\activate
   ```

3. Instala dependencias si es necesario:
   ```powershell
   pip install django
   ```

4. Aplica migraciones:
   ```powershell
   .\venv\Scripts\python.exe manage.py migrate
   ```

5. Ejecuta el servidor de desarrollo:
   ```powershell
   .\venv\Scripts\python.exe manage.py runserver
   ```

6. Abre el navegador en:
   ```text
   http://127.0.0.1:8000/
   ```

7. Para acceder al admin de Django, usa:
   ```text
   http://127.0.0.1:8000/admin/
   ```

## Estructura principal

- `models.py`: modelos `Autor`, `Libro` y `Resena`.
- `admin.py`: registro de los modelos en el panel de administración.
- `urls.py`: rutas internas para la app.
- `views.py`: vista de inicio.
- `templates/biblioteca/`: plantillas para la app.
