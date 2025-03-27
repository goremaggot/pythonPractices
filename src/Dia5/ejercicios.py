def devolver_distintos(uno, dos, tres):
    suma = 0
    suma = uno + dos + tres
    mayor = 0
    menor = 0
    numeromayor = 0
    numeromenor = 0
    if uno > dos and uno > tres:
        mayor = uno
        numeromayor = 1
    elif dos > uno and dos > tres:
        mayor = dos
        numeromayor = 2
    else:
        mayor = tres
        numeromayor = 3
    if uno < dos and uno < tres:
        menor = uno
        numeromenor = 1
    elif dos < uno and dos < tres:
        menor = dos
        numeromenor = 2
    else:
        menor = tres
        numeromenor = 3
    numerointermedio = 0
    if numeromayor == 1 and numeromenor == 2:
        numerointermedio = tres
    elif numeromayor == 1 and numeromenor == 3:
        numerointermedio = dos
    elif numeromayor == 2 and numeromenor == 1:
        numerointermedio = tres
    elif numeromayor == 2 and numeromenor == 3:
        numerointermedio = uno
    elif numeromayor == 3 and numeromenor == 1:
        numerointermedio = dos
    elif numeromayor == 3 and numeromenor == 2:
        numerointermedio = uno
    if suma > 15:
        return mayor
    elif suma < 10:
        return menor
    elif suma >= 10 and suma <= 15:
        return numerointermedio
    else:
        return 0


print(devolver_distintos(1, 2, 7))
print(devolver_distintos(1, 2, 14))


def devolver_distintos_senior(uno, dos, tres):
    numeros = [uno, dos, tres]
    suma = sum(numeros)
    mayor = max(numeros)
    menor = min(numeros)
    intermedio = sorted(numeros)[1]

    if suma > 15:
        return mayor
    elif suma < 10:
        return menor
    else:
        return intermedio


print(devolver_distintos_senior(1, 2, 7))
print(devolver_distintos_senior(1, 2, 14))


def devuelve_letras(palabra):
    set_palabra = set(palabra)
    list_palabra = list(set_palabra)
    list_palabra.sort()
    return list_palabra


print(devuelve_letras('hola'))
print(devuelve_letras('murcielago'))
print(devuelve_letras('mama'))


def devuelve_letras_senior(palabra):
    return sorted(set(palabra))


print(devuelve_letras_senior('hola'))
print(devuelve_letras_senior('murcielago'))
print(devuelve_letras_senior('mama'))


def contiene_cero(lista_numeros):
    return 0 in lista_numeros


print(contiene_cero([1, 2, 3, 4, 5]))
print(contiene_cero([1, 2, 3, 0, 5]))


def contar_primos(numero):
    contar = 0

    def es_primo(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primos = [n for n in range(2, numero + 1) if es_primo(n)]
    return len(primos)


print(contar_primos(10))
print(contar_primos(20))
