
# PatiApp

Este es un proyecto web con Django como backend y Vue.js como frontend. A continuación, se describen los pasos para la instalación y puesta en marcha del proyecto.

## Requisitos

Asegúrate de tener instalados los siguientes requisitos previos:

- Python 3.x
- Node.js (npm)
- Vue CLI
- pip
- npm

## Instalación

### Backend (Django)

1. **Crea un entorno virtual para el proyecto (opcional, pero recomendado):**

   ```bash
   python -m venv env
   source env/bin/activate  # En Linux o Mac
   env\Scripts\activate     # En Windows
   ```

2. **Instala las dependencias de Django:**

   ```bash
   pip install django
   pip install djangorestframework
   pip install markdown
   pip install django-filter
   pip install django-cors-headers
   ```

3. **Crea el proyecto Django:**

   ```bash
   django-admin startproject patiApp
   cd patiApp
   ```

4. **Crea tu aplicación Django (reemplaza "MODELO" con el nombre de tu aplicación):**

   ```bash
   python3 manage.py startapp MODELO
   ```

5. **Inicia el servidor Django:**

   ```bash
   python3 manage.py runserver
   ```

### Frontend (Vue.js)

1. **Instala Vue CLI globalmente (si aún no lo tienes instalado):**

   ```bash
   npm install -g @vue/cli
   ```

2. **Crea el proyecto frontend:**

   ```bash
   vue create frontend
   ```

   Sigue las instrucciones para configurar el proyecto según tus necesidades.

3. **Instala Axios para realizar solicitudes HTTP:**

   ```bash
   cd frontend
   npm install axios
   npm install chart.js

   ```

4. **Inicia el servidor de desarrollo de Vue.js:**

   ```bash
   npm run serve
   ```

Ahora deberías poder acceder al backend en `http://127.0.0.1:8000/` y al frontend en `http://localhost:8080/`.

## Notas adicionales

- Si tienes problemas con los puertos, asegúrate de que no estén siendo utilizados por otros servicios.
- Puedes agregar configuraciones adicionales para la conexión entre el frontend y el backend, como el uso de CORS o rutas específicas en `axios`.
