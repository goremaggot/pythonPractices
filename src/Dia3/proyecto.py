texto = input("Digite texto: ")
texto = texto.lower()
letras = input("Digite letras: ")
letras = letras.lower()
#cuantas veces aparece la letra que eligio
lista_letras = [item for item in letras]
lista_letras = list(set(lista_letras))
print(lista_letras)
for i,letra in enumerate(lista_letras):
    print(f"La letra {lista_letras[i]} aparece {texto.count(lista_letras[i])}")
#cuantas palabras hay en el texto
palabras = texto.split(" ")
print(f"la cantidad de palabras que hay en el texto es {len(palabras)}")
#cual es la primera y ultima letra
print(f"la primera letra del texto es {texto[0]}")
print(f"la ultima letra del texto es {texto[-1]}")
palabras.reverse()
#invertir las palabras en orden inverso
print(f"texto palabras inversas {" ".join(palabras)}")
#si la palabra python aparece en el texto
print(f"la palabra python aparece en el texto? {"python" in texto}")