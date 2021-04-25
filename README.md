# Prueba finkargo


# Instalacion

para ejecutar esta aplicacion necesitamos instalar las dependencias de `requirements.txt`, para ello necesitamos un virtual enviroment de python. 

```
$ python -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
```

# Tests

Para ejecutar pruebas unitarias ejecutar:

```
$ pytest
```

# Development server

Ejecutar el archivo `run.py` este inicializa un Flask App

```
$ python run.py
```