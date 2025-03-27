from random import randint
from random import uniform
from random import random
from random import choice
from random import shuffle

aleatorio = randint(1,50)
print(aleatorio)

aleatorio = uniform(1,50)
print(aleatorio)

aleatorio = random()
print(aleatorio)

colores = ["Rojo", "Azul", "Verde", "Amarillo", "Naranja", "Rosa", "Violeta", "Negro", "Blanco", "Gris"]

print(choice(colores))

shuffle(colores)

print(colores)