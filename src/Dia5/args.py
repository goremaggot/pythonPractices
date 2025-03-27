def suma(*args):
    return sum(args)


print(suma(1, 2, 3, 4, 5))


def suma_cuadrados(*args):
    suma = 0
    for arg in args:
        suma += (arg**2)
    return (suma)


def suma_cuadrados(*args):
    return sum(arg**2 for arg in args)


def suma_absolutos(*args):
    return (sum(abs(arg) for arg in args))


def numeros_persona(nombre, *numeros):
    suma_numeros = sum(numeros)
    return f"{nombre}, la suma de tus números es {suma_numeros}"


numeros_persona("Juan", 1, 2, 3, 4, 5)
