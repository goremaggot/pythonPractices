x = 2
y = 4
z = 3
xx = 3.22222222222222222222222222222222222222222222
print(f"{x} mas {y} es igual a {x+y}")
print(f"{x} menos {y} es igual a {x-y}")
print(f"{x} por {y} es igual a {x*y}")
print(f"{x} dividido {y} es igual a {x/y}")
print(f"{x} dividido al piso  o cociente de {y} es igual a {x//y}")
print(f"{z} modulo de  {y} es igual a {z%y}")
print(f"{y} elevado a la {y} es igual a {y**y}")
print(f"la raiz cuadrada de {y} es igual a {round(y**0.5)}")
print(f"El redondeo con dos decimales de {xx} es igual a {round(xx,2)}")

nombre = input("Digita tu nombre: ")

while True:
    ventas = input("Digite el total de ventas: ")
    try:
        ventas = float(ventas)  # Intentamos convertir a float
        break  # Si tiene éxito, salimos del bucle
    except ValueError:
        print("Por favor, ingrese un número válido.")

comision = ventas * 0.13
print(f"El total de la comisión para {nombre} es {round(comision, 2)}")
