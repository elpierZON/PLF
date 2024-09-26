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

print ("Lista de numeros")
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i, l in enumerate(lista):
    print(i , l)

#lista iterada
print("------------Lista de iterada---------")
lista1 = [20, 18, 19, 20]
lista2 = ["Juan","Martin","Jose","Pepe", ]

for l1,l2 in zip (lista,lista2): #zip sirve para unir 2 o mas listas
    print(l1,l2)

#Escribir un programa que permita iterar iterar las listas usando los índices como hemos visto al principio, y 
# haciendo uso de Len(), que nos devuelva la longitud de la lista 

print ("Iterando listas con longitud ")
lista4 = ["Juan","Martin","Jose","Pepe","Tito" ]

len_lista4 = len(lista4)

for i,l in enumerate(lista4):
    print(i,l,len_lista4)

#EJERCICIO 02:
#Escribir una función que reciba una lista de notas y devuelva la lista de calificaciones correspondientes a esas notas.

def notas_a_calificaciones(notas):
    calificaciones = []
    for i in notas:
        if 18 <= i <= 20:
            calificacion = "Excelente"
        elif 14 <= i < 18:
            calificacion = "Bueno"
        elif 10 <= i < 14:
            calificacion = "Suficiente"
        else:
            calificacion = "Insuficiente"

        calificaciones.append(calificacion)

    return calificaciones
notas = [20, 18, 13, 10, 7]
resultado = notas_a_calificaciones(notas)
print(resultado)  


# Escribir una función que simule una calculadora científica que permita calcular el seno, coseno, tangente, exponencial y logaritmo neperiano. 
# La función preguntará al usuario el valor y la función a aplicar, y mostrará por pantalla una tabla con los enteros de 1 al valor introducido 
# y el resultado de aplicar la función a esos enteros.

print("CALCULADORA CIENTIFICA")

def calculadora_cientifica():
    numero = int(input("Ingrese un numero a maximo "))
    print("elige la operacion: ")
    print("1: Seno")
    print("2: Coseno")
    print("3: Tangente")
    print("4: Exponencial")
    print("5: Logaritmo Neperiano")
    operacion = int(input("Introduzca el numero de la operacion deseada"))

    if operacion==1:

        
    


calculadora_cientifica()    