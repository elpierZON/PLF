
def problema1():
    lista = input("ingrese las palabras separadas por espacio: ").split()
    print(lista)

    sustituir = input("ingrese la palabra a sustituir: ")
    nueva_palabra= input("ingrese la nueva palabra: ")

    for i in range(len(lista)):
        if lista[i] == sustituir : lista[i] = nueva_palabra

    print(lista) 

def eliminar_repeticiones(lista):
    return list(set(lista))

def crear_listas():
    # Pedir al usuario que ingrese las dos listas de palabras
    lista1 = input("Introduce palabras para la primera lista, separadas por espacios: ").split()
    lista2 = input("Introduce palabras para la segunda lista, separadas por espacios: ").split()

    # Eliminar elementos repetidos en cada lista
    lista1 = eliminar_repeticiones(lista1)
    lista2 = eliminar_repeticiones(lista2)

    # Convertir las listas en conjuntos para realizar operaciones de conjuntos
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    # Lista de palabras que aparecen en las dos listas
    interseccion = list(conjunto1.intersection(conjunto2))

    # Lista de palabras que aparecen en la primera lista, pero no en la segunda
    solo_en_primera = list(conjunto1.difference(conjunto2))

    # Lista de palabras que aparecen en la segunda lista, pero no en la primera
    solo_en_segunda = list(conjunto2.difference(conjunto1))

    # Lista de palabras que aparecen en ambas listas
    union = list(conjunto1.union(conjunto2))

    # Mostrar los resultados
    print("\nPalabras que aparecen en ambas listas (sin repeticiones):", interseccion)
    print("Palabras que aparecen solo en la primera lista:", solo_en_primera)
    print("Palabras que aparecen solo en la segunda lista:", solo_en_segunda)
    print("Todas las palabras que aparecen en ambas listas:", union)
crear_listas()
# Llamar a la función principal


def decimales():
    # Solicitar al usuario el nombre del producto
    nombre_producto = input("Ingrese el nombre del producto: ")

    # Solicitar al usuario el precio del producto
    precio_producto = float(input("Ingrese el precio del producto: "))

    # Solicitar al usuario el número de unidades del producto
    num_unidades = int(input("Ingrese el número de unidades: "))

    # Calcular el coste total
    coste_total = precio_producto * num_unidades

    # Formatear y mostrar la cadena con el nombre del producto, precio unitario, número de unidades y coste total
    print(f"{nombre_producto}: {precio_producto:09.2f} {num_unidades:03d} {coste_total:011.2f}")



def suma():
    n=int(input("ingrese un numero : "))
    suma = n*(n+1)/2
    print(f"la suma de los primeros numeros enteros desde el 1 hasta {n} es {suma}")


def alreves():
    cadena = input("ingrese una cadena: ")
    print(cadena[::-1])
    lista= input("Ingrese palabras").split()
    print(lista[::-1])

#alreves()   