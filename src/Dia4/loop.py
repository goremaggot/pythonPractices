mi_tupla = (1, 2, 3, 4, 5)
mi_lista = ['a', 'b', 'c', 'd']
nombres = ['Raul','Ricardo',"Sandra","Daniel","Romulo"]
for elemento in mi_tupla:  # Tupla no usa index
    print(elemento)
for elemento in mi_lista:
    numero = mi_lista.index(elemento) + 1
    print(f"Letra {elemento} numero: {numero}")
for elemento in nombres:
    if elemento.lower().startswith('r'):
        print(elemento)
for objeto in [[1,2],[3,4],[5,6]]:
    print(objeto)
for a,b in [[1, 2], [3, 4], [5, 6]]:
    print(a)
    print(b)
for objeto1 in [[1, 2], [3, 4], [5, 6]]:
    for objeto2 in objeto1:
        print(objeto2)

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0
for numero in lista_numeros:
    if numero%2 == 0:
        suma_pares = suma_pares + numero
    else:
        suma_impares = suma_impares + numero
print("Suma pares "+ str(suma_pares))
print("Suma impares " + str(suma_impares))

stop = True
numero = 10
while stop:
    print(numero)
    numero = numero - 1
    if numero == 0:
        stop = False
else:
    print("Termino")

for numero in range(20,30):
    print(numero)

saldo = 1000  # Saldo inicial

while True:
    print("\n💰 Cajero Automático")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print(f"Su saldo actual es: ${saldo}")
    elif opcion == "2":
        monto = int(input("Ingrese el monto a retirar: "))
        if monto > saldo:
            print("❌ Saldo insuficiente.")
        else:
            saldo -= monto
            print(f"✅ Retiro exitoso. Su nuevo saldo es: ${saldo}")
    elif opcion == "3":
        print("👋 Gracias por usar el cajero. ¡Hasta luego!")
        break
    else:
        print("❌ Opción no válida. Intente de nuevo.")

# Abrimos un archivo para escribir las tablas
with open("tablas_de_multiplicar.txt", "w") as archivo:
    for numero in range(1, 11):  # Iteramos del 1 al 10
        archivo.write(f"📌 Tabla del {numero}\n")
        for multiplicador in range(1, 11):  # Multiplicamos del 1 al 10
            archivo.write(f"{numero} x {multiplicador} = {numero * multiplicador}\n")
        archivo.write("\n")  # Agregamos un salto de línea entre tablas

print("✅ Se han generado las tablas de multiplicar en 'tablas_de_multiplicar.txt'")

estudiantes = ["Ana", "Carlos", "Beatriz", "David", "Elena"]

nombre = input("Ingrese el nombre del estudiante a buscar: ")

for i, estudiante in enumerate(estudiantes):
    if estudiante.lower() == nombre.lower():
        print(f"✅ {nombre} está en la posición {i}.")
        break
else:
    print("❌ Nombre no encontrado.")

lista=[]
for i,letra in enumerate("Python"):
    lista.append((i,letra))
print(lista)