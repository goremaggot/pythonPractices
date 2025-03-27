usuarios = ["u001", "u002", "u003"]
nombres = ["Carlos Pérez", "Ana López", "Luis Rojas"]
correos = ["carlos@email.com", "ana@email.com", "luis@email.com"]

# Crear una lista de diccionarios
datos_usuarios = [{"id": u, "nombre": n, "email": e} for u, n, e in zip(usuarios, nombres, correos)]

print(datos_usuarios)

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
for a, b in zip(paises,capitales):
    print(f"La capital de {a} es {b}")

espanol = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]

numeros = list(zip(espanol, portugues, ingles))

print(numeros)