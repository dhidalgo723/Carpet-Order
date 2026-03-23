# Organizador Automático de Directorios

Este es un proyecto que desarrollé para solucionar un problema real: el caos en mi carpeta de "Descargas". Es un script de automatización en Python que clasifica archivos automáticamente en subcarpetas específicas según su tipo (Documentos, Imágenes, Videos, etc.).

## ¿Por qué usé estas librerías?
Para este proyecto decidí usar exclusivamente librerías nativas de Python:
1. **`os`**: La utilicé para interactuar con el sistema operativo, crear carpetas y listar los archivos del directorio.
2. **`shutil`**: Es la herramienta ideal para mover archivos de forma segura entre rutas. 

Al usar librerías estándar, el script es extremadamente ligero y no requiere que el usuario instale dependencias externas, lo que facilita su portabilidad.

## Lógica detrás del código
Elegí una estructura basada en un **diccionario de formatos** por varias razones:
1. **Escalabilidad:** Si mañana quiero que el script también organice archivos de audio (.mp3), solo tengo que añadir una línea al diccionario en lugar de modificar toda la lógica.
2. **Eficiencia:** En lugar de hacer mil condicionales `if/else`, uso un bucle que recorre las extensiones. Esto hace que el código sea más limpio y fácil de leer (Clean Code).
3. **Seguridad:** Añadí una verificación `os.path.isdir` para asegurarme de que el script no intente mover carpetas dentro de otras carpetas, evitando bucles infinitos.