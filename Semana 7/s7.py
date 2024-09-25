#para que nos imprima las cadenas
mensaje = "Hola Ernesto"
subcadena = mensaje[0:9]
subcadena1 = mensaje[1:9]
subcadena2 = mensaje[2:7]
subcadena3 = mensaje[0:8]

print(subcadena)
print(subcadena1)
print(subcadena2)
print(subcadena3)

# --------------Listas---------------
#Escribir un programa que imprima una lista acompañado de su indice, que tome valores desde o hasta n-1


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for indice, valor in enumerate(lista):
    print(f"{indice} - {valor}")
