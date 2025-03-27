# Ejemplo 1: Uso básico de match en Python
def ejemplo_basico(valor):
    match valor:
        case 1:
            return "Uno"
        case 2:
            return "Dos"
        case 3:
            return "Tres"
        case _:
            return "Otro valor"

print(ejemplo_basico(1))  # Salida: Uno
print(ejemplo_basico(4))  # Salida: Otro valor

# Ejemplo 2: Comprobación de la estructura de un diccionario
def comprobar_diccionario(diccionario):
    match diccionario:
        case {"nombre": str(nombre), "edad": int(edad)}:
            return f"Nombre: {nombre}, Edad: {edad}"
        case {"nombre": str(nombre)}:
            return f"Nombre: {nombre}, Edad no especificada"
        case _:
            return "Estructura de diccionario no reconocida"

print(comprobar_diccionario({"nombre": "Andrés", "edad": 30}))  # Salida: Nombre: Andrés, Edad: 30
print(comprobar_diccionario({"nombre": "Andrés"}))  # Salida: Nombre: Andrés, Edad no especificada
print(comprobar_diccionario({"edad": 30}))  # Salida: Estructura de diccionario no reconocida