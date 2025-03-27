def saludar_persona(nombre=""):
    print("Hola, ¿cómo estás? " + nombre)


saludar_persona("Pajuelo")


def cuadrado(un_numero):
    print(un_numero ** 2)


cuadrado(5)


def multiplicar(a, b):
    return a * b


resultado = multiplicar(5, 3)
print(resultado)


def invertir_palabra(palabra):
    return palabra[::-1].upper()


palabra = "Python"
print(invertir_palabra(palabra))
