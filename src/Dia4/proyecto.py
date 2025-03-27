from random import randint
nombre = input("¿Cuál es tu nombre? ")
print(f"Bueno, {nombre}, he pensado un número entre 1 y 100, y tienes solo ocho intentos  para adivinar cuál crees que es el número.")
numeror = randint(1, 100)
intentos = 1
while True:
    try:
        numero = int(input("¿Cuál es tu número? "))
        match numero:
            case numero if numero not in range(1, 101):
               print("El número debe estar entre 1 y 100.")
            case numero if numero < numeror:
               print("Respuesta incorrecta ha elegido un número menor al número secreto")
            case numero if numero > numeror:
               print("Respuesta incorrecta ha elegido un número mayor al número secreto")
            case numero if numero == numeror:
               print(f"¡Felicidades! Has adivinado el número secreto en {intentos} intentos.")
               break
        intentos += 1
        if intentos > 8:
           print(f"Lo siento, {nombre}, has agotado tus intentos. El número secreto era {numeror}.")
           break
    except ValueError:
        print("Por favor, ingrese un número válido.")
