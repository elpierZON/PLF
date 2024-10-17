#1.	Escriba un programa que permita crear una lista de palabras. Para ello, 
# el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista. 
# Por último, el programa tiene que escribir la lista.

def problema1():
    numero = int(input("Ingrese un numero:"))
    lista = []
    for i in range(numero):
        palabra = input("Ingrese una palabra:")
        lista.append(palabra)
    print(lista)
#problema1()

#2.	Escriba un programa que permita crear una lista de palabras y que, 
# a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.
def problema2():
    lista =input("ingrese las palabras separadas por espacio: ").split()
    pedir_palabra = input("ingrese la palabra a buscar: ")
    print(lista)
    contador = lista.count(pedir_palabra)
    print (f"La palabra {pedir_palabra} aparece {contador} veces en la lista")
#problema2()

#3.	Escriba un programa que permita crear una lista de palabras y que, a continuación, 
# pida dos palabras y sustituya la primera por la segunda en la lista.

def problema3():
    lista = input("ingrese las palabras separadas por espacio:").split()
    print(lista)
    sustituir = input("ingrese la palabra a sustituir:")
    nueva_palabra = input("ingrese la nueva palabra:")
    for i in range(len(lista)):
        if lista[i] == sustituir : lista[i] = nueva_palabra
    print(lista)
problema3()


#4.	Escriba un programa que permita crear una lista de palabras y que, 
# a continuación, pida una palabra y elimine esa palabra de la lista.
def problema4():
    lista = input("ingrese las palabras separadas por espacio:").split()
    print(lista)
    palabra = input("ingrese la palabra a eliminar:")
    lista.remove(palabra)
    print(lista)
#problema4()


#5.	Escriba un programa que permita crear dos listas de palabras y que, a continuación,
#  elimine de la primera lista los nombres de la segunda lista.

def problema5():
    lista1 = input("ingrese las palabras separadas por espacio para la lista 1:").split()
    lista2 = input("ingrese las palabras separadas por espacio para la lista 2:").split()
    for palabra in lista1:
        while palabra in lista2:
            lista2.remove(palabra)
    print(lista1)

#6.	Escriba un programa que permita crear una lista de palabras y que, a continuación, 
# cree una segunda lista igual a la primera, pero al revés 
# (no se trata de escribir la lista al revés, sino de crear una lista distinta).
def problema6():
    lista1 = input("ingrese las palabras separadas por espacio para la lista :").split()
    lista2 = lista1[::-1]
    print( f"la lista original es: {lista1}")
    print(f"la lista invertida es: {lista2}")
#problema6()

#7.	Escriba un programa que permita crear una lista de palabras y que, a 
# continuación, elimine los elementos repetidos 
# (dejando únicamente el primero de los elementos repetidos).
def problema7():
    # Solicitar al usuario que ingrese un número
    lista = input("Ingrese las palabras separadas por espacio: ").split()
    
    # Crear una nueva lista para almacenar las palabras sin duplicados
    lista_sin_duplicados = []
    
    # Recorrer la lista original y agregar cada palabra a la nueva lista solo si no está ya en la nueva lista
    for palabra in lista:
        if palabra not in lista_sin_duplicados:
            lista_sin_duplicados.append(palabra)
    
    # Mostrar la lista sin duplicados
    print("Lista sin duplicados:", lista_sin_duplicados)


#problema7()

#8.	Escriba un programa que permita crear dos listas de palabras y que, a continuación, escriba las siguientes listas (en las que no debe haber repeticiones):
#Lista de palabras que aparecen en las dos listas.
#	Lista de palabras que aparecen en la primera lista, pero no en la segunda.
#	Lista de palabras que aparecen en la segunda lista, pero no en la primera.
#	Lista de palabras que aparecen en ambas listas.
#Nota: Para evitar las repeticiones, el programa deberá empezar eliminando los elementos repetidos en cada lista.


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
#crear_listas()
# Llamar a la función principal

#9.	Escribir un programa que pregunte el nombre de un producto, 
# su precio y un número de unidades y muestre por pantalla 
# una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 
# 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales 
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


    