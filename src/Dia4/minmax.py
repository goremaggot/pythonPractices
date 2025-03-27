palabras = ["manzana", "banana", "cereza", "kiwi", "mango"]

# Encontrar la palabra más pequeña y la más grande alfabéticamente
palabra_minima = min(palabras)
palabra_maxima = max(palabras)

print(f"La palabra alfabéticamente más pequeña es: {palabra_minima}")
print(f"La palabra alfabéticamente más grande es: {palabra_maxima}")

from datetime import datetime

fechas = [
    datetime(2023, 5, 1),
    datetime(2022, 8, 15),
    datetime(2025, 1, 1),
    datetime(2021, 7, 20)
]

# Encontrar la fecha más antigua y la más reciente
fecha_minima = min(fechas)
fecha_maxima = max(fechas)

print(f"La fecha más antigua es: {fecha_minima.strftime('%d/%m/%Y')}")
print(f"La fecha más reciente es: {fecha_maxima.strftime('%d/%m/%Y')}")

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades.keys())
print(edad_minima)
print(ultimo_nombre)