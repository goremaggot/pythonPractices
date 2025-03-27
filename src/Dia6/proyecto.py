import os


def validar_opcion(opcion: str) -> bool:
    return opcion.isdigit() and 1 <= int(opcion) <= 6


def validar_opcion_dict(categorias: dict, opcion: str) -> bool:
    return opcion.isdigit() and int(opcion) in categorias.keys()


def obtener_ruta() -> str:
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "Recetas")


def obtener_cantidad_recetas(ruta_recetas: str) -> int:
    total_archivos = 0
    for _, _, files in os.walk(ruta_recetas):
        total_archivos += len(files)
    return total_archivos


def print_dict(diccionario: dict) -> None:
    for key, value in diccionario.items():
        print(f"{key}. {value}")


def get_carpetas(ruta: str) -> dict:
    categorias = os.listdir(ruta)
    return {i+1: categoria for i, categoria in enumerate(categorias)}


def get_archivos(ruta: str) -> dict:
    recetas = [os.path.splitext(receta)[0] for receta in os.listdir(ruta)]
    return {i+1: receta for i, receta in enumerate(recetas)}


def leer_receta() -> None:
    ruta = obtener_ruta()
    categorias = get_carpetas(ruta)
    while True:
        print_dict(categorias)
        opcion_categoria = input("Seleccione una categoria: ")
        if validar_opcion_dict(categorias, opcion_categoria):
            categoria = categorias[int(opcion_categoria)]
            rutacategoria = os.path.join(ruta, categoria)
            recetas = get_archivos(rutacategoria)
            while True:
                if len(recetas) == 0:
                    print("No hay recetas en esta categoria")
                    input("Presione enter para continuar...")
                    return
                else:
                    print_dict(recetas)
                    opcion_receta = input("Seleccione una receta: ")
                    if validar_opcion_dict(recetas, opcion_receta):
                        receta = recetas[int(opcion_receta)]
                        archivo_path = os.path.join(
                            rutacategoria, f"{receta}.txt")
                        with open(archivo_path, "r", encoding="utf-8") as archivo:
                            print(f"Receta seleccionada: {receta}")
                            print(archivo.read())
                        input("Presione enter para continuar...")
                        return
                    else:
                        print("Opción no válida")
        else:
            print("Opción no válida")


def crear_receta() -> None:
    ruta = obtener_ruta()
    categorias = get_carpetas(ruta)
    while True:
        print_dict(categorias)
        opcion_categoria = input("Seleccione una categoria: ")
        if validar_opcion_dict(categorias, opcion_categoria):
            categoria = categorias[int(opcion_categoria)]
            crea_receta_texto(categoria)
            return
        else:
            print("Opción no válida")


def crea_receta_texto(categoria: str) -> None:
    print("Creando receta")
    ruta = os.path.join(obtener_ruta(), categoria)
    while True:
        nombre_receta = input("Ingrese el nombre de la receta: ").lower()
        archivo_path = os.path.join(ruta, f"{nombre_receta.capitalize()}.txt")
        if os.path.exists(archivo_path):
            print("El archivo ya existe")
            input("Presione enter para continuar...")
        else:
            receta = input("Ingrese la receta: ")
            with open(archivo_path, "w", encoding="utf-8") as archivo:
                archivo.write(receta)
            print("Receta creada")
            input("Presione enter para continuar...")
            break


def main() -> None:
    while True:
        print("Bienvenido al recetario")
        ruta_recetas = obtener_ruta()
        print(f"La ruta que tiene las recetas es: {ruta_recetas}")
        print(f"El total de Categorias es: {len(os.listdir(ruta_recetas))}")
        print(
            f"El total de recetas es: {obtener_cantidad_recetas(ruta_recetas)}")
        print("1. Leer receta")
        print("2. Crear receta")
        print("3. Crear categoria")
        print("4. Eliminar receta")
        print("5. Eliminar categoria")
        print("6. Salir")

        opcion = input("Seleccione una opcion: ")
        if validar_opcion(opcion):
            opcion = int(opcion)
            if opcion == 1:
                leer_receta()
            elif opcion == 2:
                crear_receta()
            elif opcion == 3:
                crear_categoria()
            elif opcion == 4:
                eliminar_receta()
            elif opcion == 5:
                eliminar_categoria()
            elif opcion == 6:
                print("Saliendo...")
                break
        else:
            print("Opción no válida")


def crear_categoria() -> None:
    ruta = obtener_ruta()
    while True:
        categoria = input("Ingrese el nombre de la categoria: ")
        if not categoria.isalpha():
            print("La categoria solo debe contener letras")
            input("Presione enter para continuar...")
        else:
            categoria_path = os.path.join(ruta, categoria.capitalize())
            if os.path.exists(categoria_path):
                print("La categoria ya existe")
                input("Presione enter para continuar...")
            else:
                os.mkdir(categoria_path)
                print("Categoria creada")
                input("Presione enter para continuar...")
                break


def eliminar_receta() -> None:
    ruta = obtener_ruta()
    categorias = get_carpetas(ruta)
    while True:
        print_dict(categorias)
        opcion_categoria = input("Seleccione una categoria: ")
        if validar_opcion_dict(categorias, opcion_categoria):
            categoria = categorias[int(opcion_categoria)]
            eliminar_receta_texto(categoria)
            return
        else:
            print("Opción no válida")


def eliminar_receta_texto(categoria: str) -> None:
    ruta = os.path.join(obtener_ruta(), categoria)
    recetas = get_archivos(ruta)
    while True:
        if len(recetas) == 0:
            print("No hay recetas en esta categoria")
            input("Presione enter para continuar...")
            return
        else:
            print_dict(recetas)
            opcion_receta = input("Seleccione una receta para eliminar: ")
            if validar_opcion_dict(recetas, opcion_receta):
                receta = recetas[int(opcion_receta)]
                archivo_path = os.path.join(
                    ruta, f"{receta.capitalize()}.txt")
                if not os.path.exists(archivo_path):
                    print("La receta no existe")
                    input("Presione enter para continuar...")
                    return
                else:
                    os.remove(archivo_path)
                    print("Receta eliminada")
                    input("Presione enter para continuar...")
                    return
            else:
                print("Opción no válida")


def eliminar_categoria() -> None:
    ruta = obtener_ruta()
    categorias = get_carpetas(ruta)
    while True:
        print_dict(categorias)
        opcion_categoria = input("Seleccione una categoria para eliminar: ")
        if validar_opcion_dict(categorias, opcion_categoria):
            categoria = categorias[int(opcion_categoria)]
            categoria_path = os.path.join(ruta, categoria)
            if not os.path.exists(categoria_path):
                print("La categoria no existe")
                input("Presione enter para continuar...")
            else:
                os.rmdir(categoria_path)
                print("Categoria eliminada")
                input("Presione enter para continuar...")
                return
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
