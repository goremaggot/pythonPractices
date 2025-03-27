import os

# Crear un archivo y escribir en él


def crear_y_escribir_archivo(ruta, contenido):
    with open(ruta, 'w') as archivo:
        archivo.write(contenido)
    print(f"Archivo creado y escrito en: {ruta}")

# Leer el contenido de un archivo


def leer_archivo(ruta):
    with open(ruta, 'r') as archivo:
        contenido = archivo.read()
    print(f"Contenido del archivo {ruta}:\n{contenido}")
    return contenido

# Añadir contenido a un archivo existente


def anadir_a_archivo(ruta, contenido):
    with open(ruta, 'a') as archivo:
        archivo.write(contenido)
    print(f"Contenido añadido al archivo: {ruta}")

# Eliminar un archivo


def eliminar_archivo(ruta):
    if os.path.exists(ruta):
        os.remove(ruta)
        print(f"Archivo eliminado: {ruta}")
    else:
        print(f"El archivo {ruta} no existe")


# Ejemplos de uso
ruta_archivo = '/home/andres/PycharmProjects/PythonProject/Dia6/ejemplo.txt'
contenido_inicial = "Este es el contenido inicial del archivo.\n"
contenido_adicional = "Este es contenido adicional.\n"

crear_y_escribir_archivo(ruta_archivo, contenido_inicial)
leer_archivo(ruta_archivo)
anadir_a_archivo(ruta_archivo, contenido_adicional)
leer_archivo(ruta_archivo)
eliminar_archivo(ruta_archivo)
