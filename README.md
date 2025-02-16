# ACTIVITAT 13
URL centres/students (proyecto)
![Alumnat](/ACTIVITAT_13/imagenes/rutaalumnat.png)

URL centres/teachers (proyecto)
![Professorat](/ACTIVITAT_13/imagenes/rutaprofe.png)

# ACTIVITAT 14
### 1. Configuración proyecto
Configuración de la base de datos
![Settings.py](/ACTIVITAT_13/imagenes/databases.png)

Configuración templates 
![Settings.py](/ACTIVITAT_13/imagenes/templates.png)

Aplicación añadida a installed_apps
![Settings.py](/ACTIVITAT_13/imagenes/aplicacio.png)

### 2. Creación nueva aplicación
Urls para la llamada de los métodos
![urls.py aplicación](/ACTIVITAT_13/imagenes/urls.png)

Urls añadidos a urls.py del proyecto principal
![urls.py proyecto](/ACTIVITAT_13/imagenes/urlsproyecto.png)

### 3. Creación modelo de la aplicación
Comando de las migraciones
![Comandos migrate](/ACTIVITAT_13/imagenes/comandosmigrate.png)

Vista base de datos después de las migraciones
![Tablas creadas en la base de datos](/ACTIVITAT_13/imagenes/BaseDatos.png)

### 4. Login sin sessión
![Login sin sessión](/ACTIVITAT_13/imagenes/sinsesion.png)
- El usuario ingresa su email y contraseña.
- Si las credenciales son correctas, se redirige al usuario a la página de inicio.
- Si las credenciales son incorrectas, se muestra un mensaje de error.

### 5. Login con sessión
![Login sin sessión](/ACTIVITAT_13/imagenes/consesion.png)
- El usuario ingresa su email y contraseña.
- Si las credenciales son correctas, se guarda la información en la sesión.
- El usuario no necesita volver a iniciar sesión mientras la sesión esté activa.

### 5. Logout
- El usuario puede cerrar sesión, lo que elimina toda la información de la sesión.
- Después de hacer logout, el usuario es redirigido a la página de login.