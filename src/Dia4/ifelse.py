mascota = 'perro'
edad = 5
if mascota == 'gato':
    print("Tienes un gato")
    if edad < 10:
        print("Es un Kiiten")
    else:
        print("Es adulto")
elif mascota == 'perro':
    print("Tienes un perro")
    if edad < 10:
        print("Es un cachorro")
    else:
        print("Es adulto")
else:
    print("Que animal tienes?")

edad = 16
tiene_licencia = False

if edad >= 18:
    if tiene_licencia:
        print("Puedes conducir")
    else:
        print("No puedes conducir. Necesitas contar con una licencia")
else:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
