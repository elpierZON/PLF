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