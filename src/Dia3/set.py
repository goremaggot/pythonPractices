# no almacena listas ni diccionarios porque no son inmutables solo tuplas
mi_set = set({1, 2, 3, 4, (1, 2, 3), 5})
print(mi_set)
print(2 in mi_set)
mi_set2 = {1, 7, 8}
mi_set2.update(mi_set)  # update cuando es mas de un valor
mi_set2.add(10)  # add cuando es un solo valor
print(mi_set2)
mi_set2.discard(5)
aleatorio = mi_set2.pop()  # NO usar elimina un elemento aleatorio aunque por lo que veo elimina el primero mejor usar discard
print(aleatorio)
mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}
mi_set_3 = mi_set_1.union(mi_set_2)
mi_set_3 = mi_set_1 | mi_set_2