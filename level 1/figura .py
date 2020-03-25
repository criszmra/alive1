#inputs
from math import sqrt
print ("Area de la figura")
r = int(input("Medida radio: "))
h = int(input("Medida hipotenusa: "))

#proceso

base = r+r
altura = sqrt (h**2 - r**2)
triangulo = (base*altura)/2

circulo = (r**2 * 3.1416)/2


total = triangulo + circulo
#output

print (f"Este es el total: {total}")
