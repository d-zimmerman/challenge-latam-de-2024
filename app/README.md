# App

## Pasos previos

1. Tener instalado Docker
2. Colocar el archivo JSON que se quiera leer en el directorio `data/`
3. [Opcional] Modificar la constante `FILENAME` dentro de `app/main.py` si es que el nombre del archivo es distinto. Si se ejecutará por Jupyter, esto se podrá cambiar en la celda de la notebook `src/challenge.ipynb`.

## Encendido

Esta documentación sirve para poder correr el proyecto. Cabe destacar que existen dos modos de ejecución:
1. Ejecutar container de Docker y trabajar por CLI.
2. Ejecutar Jupyter Notebook y trabajar por interfaz de Jupyter.

Para cada una de estas opciones dejo el paso a paso para poder correr el proyecto

### Docker + CLI

1. Desde la raíz del proyecto correr el comando para encender el container

```
docker compose -f docker/docker-compose.dev.yml up --build -d
```

2. Luego de correr el comando para ingresar al container

```
docker exec -it app_latam bash
```

3. Estando dentro del container solo es necesario correr

```
python app/main.py
```

y toda la solución se ejecutará.

### Jupyter Notebook

1. Desde la raíz del proyecto correr el comando para encender el container

```
docker compose -f docker/docker-compose.jupyter.yml up --build -d
```

2. Ir a un navegador web e ingresar a `127.0.0.1:8888`

3. Estando en la UI de Jupyter, podemos navegar por las distintas notebooks.

   En este caso ir a `src/challenge.ipynb` donde está todo el código para poder correr la solución junto con su explicación.


## Posible errores

1. Permisos para acceder al archivo `logs/app_logs.log`

La solución presenta un módulo de logging que escribe todos los logs al archivo mencionado. Puede darse la situación que el sistema local no permita la escritura, para esto deberemos modificar los permisos del directorio.

A su vez, si primero se inicia la versión `Docker + CLI` y luego se intenta correr la versión `Jupyter` puede que se genere un conflicto entre los usuarios de estos distintos containers.

Una solución rápida es eliminar el archivo y dejar que la herramienta lo cree de nuevo, iniciándola nuevamente.
