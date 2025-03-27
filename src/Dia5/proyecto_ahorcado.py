import random
import unicodedata


def valida_opcion(opcion):
    try:
        opcion = int(opcion)
        if opcion == 1:
            return True
        elif opcion == 2:
            return False
        else:
            return None
    except ValueError:
        return None


def palabra_aleatoria():
    palabras = [
        "gato", "perro", "casa", "árbol", "coche", "libro", "mesa", "silla", "ventana",
        "puerta", "flor", "jardín", "montaña", "río", "mar", "ciudad", "pueblo", "camino",
        "sol", "luna"
    ]
    # Mezclar las palabras para obtener una lista aleatoria
    random.shuffle(palabras)
    return random.choice(palabras)


def valida_palabra(letra, palabra, palabra_oculta):
    letra = letra.lower()
    letra = unicodedata.normalize('NFKD', letra).encode(
        'ASCII', 'ignore').decode('ASCII')
    palabra = unicodedata.normalize('NFKD', palabra).encode(
        'ASCII', 'ignore').decode('ASCII')
    encontro = False
    for i, l in enumerate(palabra):
        if l == letra:
            palabra_oculta[i] = letra
            encontro = True
    return palabra_oculta, encontro


def str_list_palabra(palabra):
    return " ".join(palabra)


def valida_ganador(palabra_oculta):
    return "_" not in palabra_oculta


def descuenta_intentos(intentos):
    return intentos - 1


def main():  # Número de intentos
    numero_intentos = 6  # Contador de intentos
    while True:
        print("Bienvenido al ahorcado")
        print("1. Jugar")
        print("2. Salir")
        opcion = input("Ingrese una opción: ")
        if valida_opcion(opcion):
            palabra = palabra_aleatoria()
            palabra_oculta = ["_" for _ in palabra]
            while numero_intentos != 0:
                print(
                    f"La palabra a adivinar es ({str_list_palabra(palabra_oculta)})")
                print(f"Tienes {numero_intentos} intentos")
                letra = input("Ingrese una letra: ")
                palabra_oculta, encontro = valida_palabra(
                    letra, palabra, palabra_oculta)
                if encontro:
                    print("La letra está en la palabra")
                    if valida_ganador(palabra_oculta):
                        print(f"Ganaste la palabra era {palabra}")
                        break
                else:
                    numero_intentos = descuenta_intentos(numero_intentos)
                    print(f"La letra {letra} no está en la palabra")
                    print(f"Te quedan {numero_intentos} intentos")
            if numero_intentos == 0:
                print(f"Perdiste la palabra era {palabra}")
                break
        elif valida_opcion(opcion) is None:
            print("Por favor, ingrese una opción válida.")
            continue
        else:
            break


if __name__ == "__main__":
    main()
