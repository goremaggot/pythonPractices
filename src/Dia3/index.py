texto = "Esta es una prueba"
print(texto.index("a"))
print(texto.index("a", 5))
print(texto.index("a", 11, 18))
print(texto[-4])
print(texto[5])
print(texto.rindex("a"))
print(texto.rindex("a", 1, 5))
print(texto.rindex("a", 11, 18))

texto2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(texto2[2])  # *---Esto es slicing
print(texto2[2:10])
print(texto2[2:])
print(texto2[:10])
print(texto2[2:20:2])
print(texto2[::2])
print(texto2[:2:3])
print(texto2[::-1])
print(texto2[::-2])

print(texto.upper())
print(texto.lower())
print(texto.upper())
print(texto.split(" "))
a = "Este"
b = "está"
c = "sabroso"
d = " "
e = d.join([a, b, c])
print(e)

base_url = "https://api.ejemplo.com/busqueda?"
parametros = {
    "categoria": "tecnologia",
    "pais": "es",
    "orden": "reciente"
}

query_string = "&".join(f"{k}={v}" for k, v in parametros.items())
url_final = base_url + query_string

print(url_final)

columnas = ["nombre", "edad", "ciudad"]
consulta = f"SELECT {', '.join(columnas)} FROM usuarios WHERE edad > 18;"

print(consulta)
import logging

logging.basicConfig(level=logging.INFO)

datos = ["Usuario", "ID: 1234", "Acción: Inicio de sesión"]
mensaje = " | ".join(datos)  # Unimos los datos con " | " como separador
logging.info(mensaje)

url = "https://api.ejemplo.com/busqueda?categoria=tecnologia&pais=es&orden=reciente"

# Separar la parte base de los parámetros
base_url, parametros = url.split("?")

# Dividir los parámetros en pares clave-valor
parametros_dict = dict(param.split("=") for param in parametros.split("&"))

print("Base URL:", base_url)
print("Parámetros:", parametros_dict)

lista_parametros = [item for param in parametros.split("&") for item in param.split("=")]

print(lista_parametros)

# Ejemplo de archivo de log del servidor
log_data = """INFO: Servidor iniciado
ERROR: No se puede conectar a la base de datos
INFO: Usuario autenticado
ERROR: Timeout en la conexión
WARNING: CPU a 90%"""

# Buscando errores en el log
lineas_log = log_data.split("\n")
errores = []

for i, linea in enumerate(lineas_log):
    if linea.find("ERROR") != -1:  # Si "ERROR" está en la línea
        errores.append((i, linea))  # Guardamos el índice y el mensaje

print(errores)

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
print(frase.replace("difícil", "fácil").replace("mala", "buena"))
