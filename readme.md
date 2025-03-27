# PlanOK Backend
Este proyecto es el backend de la aplicación PlanOK para administrar proyectos inmobiliarios. La API sigue los estándares RESTful y utiliza Django REST Framework junto con JWT para la autenticación y drf-spectacular para la documentación (Swagger/Redoc).

## Características
**Gestión de proyectos inmobiliarios:**
Permite listar, buscar, crear, actualizar y eliminar proyectos inmobiliarios.

**Gestión de unidades de propiedad:**
Cada proyecto puede tener varias unidades asociadas. Se pueden listar, buscar, crear, actualizar y eliminar.

**Gestión de clientes:**
Registro y administración de clientes asociados a las unidades vendidas.

**Autenticación JWT:**
Seguridad en los endpoints utilizando JWT.

**Documentación automática:**
Se genera documentación interactiva utilizando drf-spectacular (Swagger y Redoc).

**Contenerización con Docker:**
El proyecto puede ejecutarse mediante contenedores, facilitando el despliegue y la configuración.

## Requerimientos
asgiref==3.8.1
attrs==25.3.0
Django>=4.2
django-cors-headers==4.7.0
djangorestframework==3.15.2
djangorestframework_simplejwt==5.5.0
drf-spectacular==0.28.0
inflection==0.5.1
jsonschema==4.23.0
jsonschema-specifications==2024.10.1
psycopg2-binary==2.9.10
PyJWT==2.9.0
PyYAML==6.0.2
referencing==0.36.2
rpds-py==0.24.0
sqlparse==0.5.3
typing_extensions==4.13.0
tzdata==2025.2
uritemplate==4.1.1

## Build

El backend se puede ejecutar con docker, o mediante la linea de comandos.

Sin embargo el backend ya está desplegado y disponible en la siguiente URL: https://planok-backend.onrender.com

Para acceder a la documentación Swagger, visita: https://planok-backend.onrender.com/docs/

En caso de que necesiten ejecutarlo localmente, les dejo los pasos a seguir:

- Clonar el repositorio y acceder al directorio del proyecto.
- Crear y activar un entorno virtual.
- Instalar las dependencias con pip install -r requirements.txt.
- Configurar la base de datos y aplicar las migraciones con:
```
python manage.py makemigrations
python manage.py migrate
```
- Iniciar el servidor con:
```
python manage.py runserver
```

### Ejecución con docker

```
docker-compose up --build
```
