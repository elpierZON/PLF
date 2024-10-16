def suma(a,b):
    return a+b
print(suma(1,2))

#las listas permiten almacenar cualquier tipo de dato
lista=["rojo","azul","erde","amarillo",10,5,6,"Jupiter"]

#####
lista_colores=["rojo","azul","verde","Amarilo"]
print(lista_colores[1]) #azul
print(f"El 3er valor de la lista es: {lista_colores[2]}")   #verde

##ACCEDIENDO A UN CARACTER DE LA LISTA
print(lista_colores[0][1]) # o
print(f"el 2do valor con la ultima letra es: {lista_colores[1][-1]}") #l

#remplazando valor de la lista
lista_colores[1]="NAranja"
print(lista_colores)

#agregando sin reemplazarlo
lista_colores.insert(0,"morado")
print(lista_colores)


##### TUPLAS ######
#las tuplas no son mutables, en cambio las listas si

tupla= (1,2,3,4)
print(tupla)
print(tupla[0])
print(tupla[2])

tupla2=(6,7,8,9)
subtupla=tupla2[1:3]
print(f"la tupla2 es: {tupla2}")
print(f"subtupla es :{subtupla}")
print(tupla2[:-1]) 
print(tupla2[:])

#podemos convertir tuplas a listas y viceversa

lista2 = [1,2,3,4,5]
tupla2 = ("pep","juan","roberto")

print(tuple(lista2))
print(list(tupla2))


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

# Llamar a la función principal
crear_listas()
