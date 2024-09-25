def suma(a, b):
    return a + b

print(suma(3, 4))  # Siempre devolverá 7

def multiplicar_por_dos(x):
    return x * 2

def sumar_tres(x):
    return x + 3

def res(x):
    return multiplicar_por_dos(sumar_tres(x))

print(res(5))  # (5 + 3) * 2 = 16


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # 5! = 120

def aplicar_funcion(f, lista):
    return [f(x) for x in lista]

def cuadrado(x):
    return x * x

numeros = [1, 2, 3, 4]
print(aplicar_funcion(cuadrado, numeros))  # [1, 4, 9, 16]

def saludar(nombre):
    return f"Hola, {nombre}!"

print(saludar("Mundo"))  # Hola, Mundo!


# función sin parámetros o retorno de valores
def diHola():
 print("Hello!")

diHola()  # llamada a la función, 'Hello!' se muestra en la consola

# función con un parámetro
def holaConNombre(name):
  print("Hello " + name + "!")

holaConNombre("Ada")  # llamada a la función, 'Hello Ada!' se muestra en la consola

# función con múltiples parámetros con una sentencia de retorno
def multiplica(val1, val2):
  return val1 * val2

multiplica(3, 5)  # muestra 15 en la consola



# Variable global
contador = 0


def impura(a, b):
    global contador
    contador += 1
    print(f'El valor de contador es ahora {contador}')
    return a + b

# Uso de la función impura
print(impura(3, 4))  
print(impura(3, 4))  





# Función que eleva al cuadrado un número


# Uso de map con la función cuadrado
numeros = [1, 2, 3, 4, 5]
cuadrados = map(cuadrado, numeros)
print(list(cuadrados))  # Debería imprimir [1, 4, 9, 16, 25]



# Función que devuelve una función que eleva a una potencia dada
def elevar_a_la_potencia(n):
    def potencia(x):
        return x ** n
    return potencia

# Crear una función que eleva al cubo
elevar_al_cubo = elevar_a_la_potencia(3)
print(elevar_al_cubo(2))  # Debería imprimir 8




def compose(f, g):
    return lambda x: f(g(x))


# Composición de las funciones
componer = compose(multiplicar_por_dos, sumar_tres)

print(componer(5))  # Imprime 16
