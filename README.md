
# Setup

### Crear ambiente virtual
Ejecutar `py -m venv env`

### Activar el venv
> ⚠️ Puede que tengas que ejecutar el comando `Set-ExecutionPolicy Unrestricted` en caso de que no tengas la ejecución de scripts desactivada

En Windows: `./env/Scripts/Activate.ps1`

En Linux/MacOS: `source ./env/bin/activate`

### Instalar las librerias del proyecto
`pip install -r requirements.txt`


&nbsp;
# Despues de agregar una libreria

### Guardar las nuevas dependencias
`pip freeze > requirements.txt`


&nbsp;
# Al querer desarrollar

### Iniciar el ambiente virtual (por c/ sesión de terminal)
En Windows: `./env/Scripts/Activate.ps1`

En Linux/MacOS: `source ./env/bin/activate`
