# Ejemplo 1: Crear una lista de números del 0 al 9
numeros = [x for x in range(10)]
print(numeros)

# Ejemplo 2: Crear una lista de cuadrados de números del 0 al 9
cuadrados = [x**2 for x in range(10)]
print(cuadrados)

# Ejemplo 3: Crear una lista de números pares del 0 al 9
pares = [x for x in range(10) if x % 2 == 0]
print(pares)

# Ejemplo 4: Crear una lista de tuplas (número, cuadrado) para números del 0 al 9
tuplas = [(x, x**2) for x in range(10)]
print(tuplas)

# Ejemplo 5: Crear una lista de caracteres en una cadena
cadena = "Hola Mundo"
caracteres = [c for c in cadena]
print(caracteres)

# Ejemplo 6: Crear una lista de palabras en una frase
frase = "La comprensión de listas es poderosa"
palabras = [palabra for palabra in frase.split()]
print(palabras)

# Ejemplo 7: Crear una lista de números del 0 al 9 con una condición if-else
numeros_condicional = [x if x % 2 == 0 else -x for x in range(10)]
print(numeros_condicional)

# Ejemplo 8: Crear una lista de números del 0 al 9 con una condición if-elif-else
numeros_condicional_elif = [x if x % 3 == 0 else (x**2 if x % 3 == 1 else -x) for x in range(10)]
print(numeros_condicional_elif)