def todos_positivos(lista):
    for n in lista:
        if n < 0:
            return False
    return True


lista_numeros = [1, -2, 3]

print(todos_positivos(lista_numeros))


def suma_menores(lista_numeros):
    resultado = 0
    for n in lista_numeros:
        if (n in range(0, 1000)):
            resultado = resultado + n
    return resultado


print(suma_menores(lista_numeros))
