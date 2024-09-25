#Area de un cuadrado
def areaCuadrado(x):
    return x**2

#Volumen de una piramide cuadrangular
def volumenPiramideCuadrangular(a,h):
    return (areaCuadrado(a)*h)/3 


#Volumen de un prisma
def VolumenPrisma(x,h):
    return (areaCuadrado(x)*h)

resultado1 = areaCuadrado(2)
resultado2 = VolumenPrisma(2,8)
resultado3 = volumenPiramideCuadrangular(2,8)

print(f"Area del cuadrado: {resultado1}") #4
print(f"Volumen de un prisma {resultado2}") # 32
print(f"Volumen de una piramide cuadrangular {resultado3}") #10.6