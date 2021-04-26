# Prueba finkargo


# Ejecutar de forma local

para ejecutar esta aplicacion necesitamos instalar las dependencias de `requirements.txt`, para ello necesitamos un virtual enviroment de python

```sh
$ python -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
```
requiere una base de datos mongodb `version 4.2.2` o superiores, para modificar la conexión a la base de datos modificar el archivo de configuración en
`environment/environment.yml`

# Development server

Ejecutar el archivo `run.py` este inicializa un Flask App en modo demo, estara en el puerto 8080

```sh
$ python run.py
```

# Tests

Para ejecutar pruebas unitarias ejecutar:

```sh
$ pytest
```

# lanzar con docker-compose

necesitamos ejecutar el comando para lanzar los contenedores necesarios para correr la aplicación, la aplicación se ejecutara bajo el puerto 5000 en el contenedor y el mismo en el host

```sh
$ docker-compose up -d
```

# test con postman

importar el archivo `FindKargo Test.postman_collection.json` en el postman a ejecutar la prueba
todas las peticiones a la url `admin/airfreightcompanies` necesitan autenticacion el token de session se envia por la cabezera 
`x-access-tokens`, aunque el test de postman tenga precargada un token en las peticiones se recomienda realizar de nuevo la autenticacion
y copiar en cada peticion el nuevo token


