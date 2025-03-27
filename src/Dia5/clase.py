text = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
cleaned_text = text.lstrip(",:%_#")
print(cleaned_text)

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(5, "naranja")
print(frutas)

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)


def reducir_lista(lista: list[int]):
    lista = list(set(lista))
    mayor = 0
    indice = 0
    for i, n in enumerate(lista):
        if n > mayor:
            mayor = n
            indice = i
    lista.pop(indice)
    return (lista)


print(reducir_lista([1, 2, 3, 4, 5, 6, 7, 8, 9]))
