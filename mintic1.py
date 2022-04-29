import math

b = int(input("Digita la base: "))
a = int(input("Digita la altura: "))
r = int(input("Digita el radio: "))

# Buscamos el área del vagón.
def area_r(b, a):
    return b * a

# Buscamos el radio de la rueda por 2.
def area_c(r):
    return (math.pi*r*r)*2

# Atrapamos el resultado de la suma total.
res = area_c(r)+area_r(b, a)

#Imprimimos la respuesta.
print("Vagón: ", res)