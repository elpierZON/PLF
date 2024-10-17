#Escribir un programa que lea un entero positivo, n, introducido por el usuario y 
#después muestre en pantalla la suma de todos los enteros desde 1 hasta n, la 
#suma de los n primeros números positivos puede ser calculado de la siguiente 
#manera 
def suma_enteros():
    n = int(input("Ingrese un entero positivo: "))
    
    if n <= 0:
        print("El número debe ser un entero positivo.")
        return
    
    suma = n * (n + 1) // 2
    
    print(f"La suma de todos los enteros desde 1 hasta {n} es: {suma}")

#suma_enteros()

#Escribir un programa que pregunte el nombre del usuario en la consola y un 
#número entero e imprima por pantalla en líneas distintas el nombre del usuario 
#tantas veces como el número introducido.
def repetir_nombre():
    nombre = input("Ingrese su nombre: ")
    
    numero = int(input("Ingrese un número entero: "))
    
    # Imprimir el nombre del usuario tantas veces como el número introducido
    for _ in range(numero):
        print(nombre)

#repetir_nombre()
""""Una inmobiliaria de una ciudad maneja una lista de inmuebles como la siguiente:
[{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'}, {'año': 
2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'}, {'año': 1980, 
'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'}, {'año': 2005, 'metros': 
75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'}, {'año': 2015, 'metros': 90, 
'habitaciones': 2, 'garaje': False, 'zona': 'A'}] 
Construir una función que permita hacer búsqueda de inmuebles en función de 
un presupuesto dado. La función recibirá como entrada la lista de inmuebles y 
un precio, y devolverá otra lista con los inmuebles cuyo precio sea menor o igual 
que el dado. Los inmuebles de la lista que se devuelva deben incorporar un 
nuevo par a cada diccionario con el precio del inmueble, donde el precio de un 
inmueble se calcula con las siguiente fórmula en función de la zona:
 Zona A: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) 
* (1-antiguedad/100)
 Zona B: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) 
* (1-antiguedad/100) * 1.5
"""

def buscar_inmuebles(inmuebles, presupuesto):
    # Crear una lista vacía para almacenar los inmuebles que cumplen con el presupuesto
    inmuebles_en_presupuesto = []

    # Recorrer la lista de inmuebles
    for inmueble in inmuebles:
        # Calcular la antigüedad del inmueble
        antiguedad = 2023 - inmueble['año']
        
        # Calcular el precio del inmueble según la zona
        if inmueble['zona'] == 'A':
            precio = (inmueble['metros'] * 1000 + inmueble['habitaciones'] * 5000 + inmueble['garaje'] * 15000) * (1 - antiguedad / 100)
        elif inmueble['zona'] == 'B':
            precio = (inmueble['metros'] * 1000 + inmueble['habitaciones'] * 5000 + inmueble['garaje'] * 15000) * (1 - antiguedad / 100) * 1.5
        
        # Si el precio del inmueble es menor o igual al presupuesto, agregarlo a la lista resultante
        if precio <= presupuesto:
            inmueble_con_precio = inmueble.copy()
            inmueble_con_precio['precio'] = precio
            inmuebles_en_presupuesto.append(inmueble_con_precio)
    
    # Devolver la lista de inmuebles que cumplen con el presupuesto
    return inmuebles_en_presupuesto

# Ejemplo de uso
inmuebles = [
    {'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
    {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
    {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
    {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
    {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}
]

presupuesto = 150000
inmuebles_en_presupuesto = buscar_inmuebles(inmuebles, presupuesto)
for inmueble in inmuebles_en_presupuesto:
    print(inmueble)


"""Escribir una función que aplique un descuento a un precio y otra que aplique el 
IGV a un precio. Escribir una tercera función que reciba un diccionario con los 
precios y porcentajes de una cesta de la compra, y una de las funciones 
anteriores, y utilice la función pasada para aplicar los descuentos o el IGV a los 
productos de la cesta y devolver el precio final de la cesta"""

def aplicar_descuento(precio, porcentaje_descuento):
    
    return precio * (1 - porcentaje_descuento / 100)

def aplicar_igv(precio, porcentaje_igv):
    
    
    return precio * (1 + porcentaje_igv / 100)

def calcular_precio_final(cesta, funcion_aplicar):
    """
    Calcula el precio final de una cesta de la compra aplicando una función a cada producto.
    
    :param cesta: Diccionario con los precios y porcentajes de la cesta de la compra.
    :param funcion_aplicar: Función a aplicar a cada producto (aplicar_descuento o aplicar_igv).
    :return: Precio final de la cesta.
    """
    precio_final = 0
    for producto, datos in cesta.items():
        precio = datos['precio']
        porcentaje = datos['porcentaje']
        precio_final += funcion_aplicar(precio, porcentaje)
    return precio_final

# Ejemplo de uso
cesta = {
    'producto1': {'precio': 100, 'porcentaje': 10},  # 10% de descuento
    'producto2': {'precio': 200, 'porcentaje': 18},  # 18% de IGV
}

# Calcular el precio final aplicando descuentos
precio_final_descuento = calcular_precio_final(cesta, aplicar_descuento)
print(f"Precio final con descuentos: {precio_final_descuento}")

# Calcular el precio final aplicando IGV
precio_final_igv = calcular_precio_final(cesta, aplicar_igv)
print(f"Precio final con IGV: {precio_final_igv}")


""""Escriba una función que reciba otra función y una lista y devuelva otra lista con 
el resultado de aplicar la función dada a cada uno de los elementos de la lista""""

def aplicar_funcion_a_lista(funcion, lista):
    
    
    resultados = []
    
    # Recorrer la lista original y aplicar la función a cada elemento
    for elemento in lista:
        resultados.append(funcion(elemento))
    
    # Devolver la nueva lista con los resultados
    return resultados

# Ejemplo de uso
def cuadrado(x):
    return x * x

numeros = [1, 2, 3, 4, 5]
resultados = aplicar_funcion_a_lista(cuadrado, numeros)
print(resultados)  # Salida: [1, 4, 9, 16, 25]


"""""Escribir una función que reciba una lista de notas y devuelva la lista de 
calificaciones correspondientes a esas notas"""
def convertir_a_calificaciones(notas):
    """
    Convierte una lista de notas a una lista de calificaciones.
    
    :param notas: Lista de notas.
    :return: Lista de calificaciones correspondientes a las notas.
    """
    # Crear una lista vacía para almacenar las calificaciones
    calificaciones = []

    # Recorrer la lista de notas y convertir cada nota a su calificación correspondiente
    for nota in notas:
        if nota >= 90:
            calificaciones.append('A')
        elif nota >= 80:
            calificaciones.append('B')
        elif nota >= 70:
            calificaciones.append('C')
        elif nota >= 60:
            calificaciones.append('D')
        else:
            calificaciones.append('F')

    # Devolver la lista de calificaciones
    return calificaciones

# Ejemplo de uso
notas = [95, 82, 67, 58, 74]
calificaciones = convertir_a_calificaciones(notas)
print("Notas:", notas)
print("Calificaciones:", calificaciones)


"""""Escribir una función que simule una calculadora científica que permita calcular 
el seno, coseno, tangente, exponencial y logaritmo neperiano. La función 
preguntará al usuario el valor y la función a aplicar, y mostrará por pantalla una 
tabla con los enteros de 1 al valor introducido y el resultado de aplicar la función 
a esos enteros"""

import math

def calculadora_cientifica():
    # Mostrar las opciones al usuario
    print("Elija una función matemática:")
    print("1. Seno (sin)")
    print("2. Coseno (cos)")
    print("3. Tangente (tan)")
    print("4. Exponencial (exp)")
    print("5. Logaritmo neperiano (ln)")

    # Leer la opción del usuario
    opcion = int(input("Introduce el número de la función a aplicar (1-5): "))

    # Leer el valor máximo
    valor = int(input("Introduce un valor entero positivo: "))

    # Seleccionar la función matemática según la opción
    if opcion == 1:
        funcion = math.sin
        nombre_funcion = "Seno"
    elif opcion == 2:
        funcion = math.cos
        nombre_funcion = "Coseno"
    elif opcion == 3:
        funcion = math.tan
        nombre_funcion = "Tangente"
    elif opcion == 4:
        funcion = math.exp
        nombre_funcion = "Exponencial"
    elif opcion == 5:
        funcion = math.log
        nombre_funcion = "Logaritmo neperiano"
    else:
        print("Opción inválida")
        return

    # Imprimir la tabla de resultados
    print(f"\nTabla de {nombre_funcion} de 1 a {valor}:")
    print(f"{'Número':<10}{nombre_funcion:<20}")
    print("-" * 30)
    for i in range(1, valor + 1):
        resultado = funcion(i)
        print(f"{i:<10}{resultado:<20.10f}")

# Llamar a la función
#calculadora_cientifica()


"""""Escribir un programa que imprima una lista acompañado de su índice, que tome 
valores desde 0 hasta n-1"""

def imprimir_lista_con_indices():
    # Solicitar al usuario que ingrese un número entero positivo
    n = int(input("Ingrese un número entero positivo: "))
    
    # Crear una lista con valores desde 0 hasta n-1
    lista = list(range(n))
    
    # Imprimir cada valor de la lista acompañado de su índice
    for indice, valor in enumerate(lista):
        print(f"Índice: {indice}, Valor: {valor}")

# Llamar a la función para probarla
#imprimir_lista_con_indices()

"""""Escribir un programa que permita iterar 2 listas, por pantalla observaremos la 
primera lista acompañado de la lista 2"""""
def iterar_dos_listas():
    # Solicitar al usuario que ingrese la primera lista
    lista1 = input("Ingrese los elementos de la primera lista separados por espacio: ").split()
    
    # Solicitar al usuario que ingrese la segunda lista
    lista2 = input("Ingrese los elementos de la segunda lista separados por espacio: ").split()
    
    # Verificar que ambas listas tengan la misma longitud
    if len(lista1) != len(lista2):
        print("Las listas deben tener la misma longitud.")
        return
    
    # Iterar sobre ambas listas simultáneamente
    for elem1, elem2 in zip(lista1, lista2):
        print(f"{elem1} - {elem2}")

# Llamar a la función para probarla
iterar_dos_listas()


"""""Escribir un programa que permita iterar iterar las listas usando los índices como 
hemos visto al principio, y haciendo uso de Len(), que nos devuelva la longitud 
de la lista"""