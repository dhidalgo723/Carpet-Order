import os
import shutil

# Configuración de rutas (Cambia 'ruta_a_limpiar' por tu carpeta de descargas)
ruta_a_limpiar = "./Descargas_Test"
formatos = {
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Comprimidos": [".zip", ".rar", ".tar"]
}

def organizar_carpeta(directorio):
    # Creamos las subcarpetas si no existen
    for carpeta in formatos.keys():
        ruta_subcarpeta = os.path.join(directorio, carpeta)
        if not os.path.exists(ruta_subcarpeta):
            os.makedirs(ruta_subcarpeta)

    # Iteramos sobre los archivos del directorio
    for archivo in os.listdir(directorio):
        ruta_archivo = os.path.join(directorio, archivo)
        
        # Saltamos si es una carpeta
        if os.path.isdir(ruta_archivo):
            continue

        # Obtenemos la extensión del archivo
        nombre, extension = os.path.splitext(archivo)
        
        # Movemos el archivo a la carpeta correspondiente
        movido = False
        for carpeta, extensiones in formatos.items():
            if extension.lower() in extensiones:
                shutil.move(ruta_archivo, os.path.join(directorio, carpeta, archivo))
                print(f"Movido: {archivo} -> {carpeta}")
                movido = True
                break
        
        if not movido:
            print(f"Ignorado (sin categoría): {archivo}")

if __name__ == "__main__":
    # Creamos la carpeta de prueba si no existe para que puedas testearlo
    if not os.path.exists(ruta_a_limpiar):
        os.makedirs(ruta_a_limpiar)
    
    print("Iniciando organización...")
    organizar_carpeta(ruta_a_limpiar)
    print("¡Limpieza completada!")