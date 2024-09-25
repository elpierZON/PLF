# Área de un cuadrado
def areaCuadrado(x):
    return x**2

def aplicar_area_a_volumen(func_area, a, h):
    return func_area(a) * h


def volumenPiramideCuadrangular(a, h):
    return aplicar_area_a_volumen(areaCuadrado, a, h) / 3

def volumenPrisma(a, h):
    return aplicar_area_a_volumen(areaCuadrado, a, h)

# Calculando resultados
resultado1 = areaCuadrado(2)
resultado2 = volumenPrisma(2, 8)
resultado3 = volumenPiramideCuadrangular(2, 8)

print(f"Área del cuadrado: {resultado1}") # 4
print(f"Volumen de un prisma: {resultado2}") # 32
print(f"Volumen de una pirámide cuadrangular: {resultado3}") # 10.66



def clasificar_numero(num):
    return "El número es positivo" if num > 0 else "El número es no positivo"

print(clasificar_numero(5))  # El número es positivo
print(clasificar_numero(-3))  # El número es no positivo
