# Docker

En este directorio encontrarás todo lo vinculado a Docker y los archivos que necesarios para el correcto funcionamiento de este.

## Uso

### Producción

*TBD*

### Desarrollo

Al momento de desarrollar, se deberá utilizar las imágenes de Docker de desarrollo. Para ello utilizaremos el archivo `docker-compose.dev.yml` que se encargará hacer el setup de nuestros contenedores de desarrollo.

#### Encendido

Para poner a correr nuestro contenedores, seguir las siguientes instrucciones:
1. Ir a la raíz del proyecto en nuestra CLI.

    **Nota**: Asegúrese de tener instalado Docker en su entorno local antes de seguir.

2. Correr el siguiente comando por CLI.

    ```docker compose -f docker/docker-compose.dev.yml up --build -d```

   **Nota**: Una vez finalizado lo anterior, podremos usar el comando `docker ps` para validar que los contenedores están vivos.

#### Apagado

Para apagar nuestros contenedores, seguir las siguientes instrucciones:

1. Ir a la raíz del proyecto en nuestra CLI.

2. Correr el siguiente comando por CLI.

    ```docker compose -f docker/docker-compose.dev.yml down```

   **Nota**: Una vez finalizado lo anterior, podremos usar el comando `docker ps` para validar que los contenedores hayan sido apagados.

## Estructura del directorio

```
|
|---/hub : Contiene los archivos Dockerfile del proyecto.

```
