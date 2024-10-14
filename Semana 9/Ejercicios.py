#
#Escriba un programa que permita crear una lista de palabras. Para ello, el programa 
# tiene que pedir un número y luego solicitar ese número de palabras para crear la lista. 
# Por último, el programa tiene que escribir la lista.



# Solicitar al usuario el número de palabras
num_palabras = int(input("Ingrese el número de palabras: "))

# Crear una lista vacía
lista_palabras = []

# Solicitar las palabras y agregarlas a la lista
for _ in range(num_palabras):
    palabra = input("Ingrese una palabra: ")
    lista_palabras.append(palabra)

# Imprimir la lista de palabras
print("La lista de palabras es:", lista_palabras)

#Escriba un programa que permita crear una lista de palabras y que, 
# a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.

# Solicitar al usuario el número de palabras
num_palabras = int(input("Ingrese el número de palabras: "))

# Crear una lista vacía
lista_palabras = []

# Solicitar las palabras y agregarlas a la lista
for _ in range(num_palabras):
    palabra = input("Ingrese una palabra: ")
    lista_palabras.append(palabra)

# Solicitar al usuario una palabra para buscar en la lista
palabra_a_buscar = input("Ingrese la palabra a buscar: ")

# Contar cuántas veces aparece la palabra en la lista
contador = lista_palabras.count(palabra_a_buscar)

# Imprimir el número de veces que aparece la palabra en la lista
print(f"La palabra '{palabra_a_buscar}' aparece {contador} veces en la lista.")