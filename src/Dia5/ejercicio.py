from random import shuffle
from random import randint


palitos = ['-', '--', '---', '----']


def mezclar_palitos(palitos):
    shuffle(palitos)
    return palitos


def probar_suerte(numero):
    m_palitos = mezclar_palitos(palitos)
    print(m_palitos)
    if m_palitos[numero-1] == '----':
        print('Ganaste')
    else:
        print('Perdiste')


while True:
    try:
        numero = int(input("Ingrese un número del 1 al 4 (0 para salir): "))
        if numero == 0:
            break
        elif 1 <= numero <= 4:
            probar_suerte(numero)
        else:
            print("Por favor, ingrese un número entre 1 y 4.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

        def lanzar_dados():
            dado1 = randint(1, 6)
            dado2 = randint(1, 6)
            return dado1, dado2
