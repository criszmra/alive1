#inputs
from math import sqrt
def figura (h,r):
    base = r+r
    altura = sqrt (h**2 - r**2)
    triangulo = (base*altura)/2
    circulo = (r**2 * 3.1416)/2

    total = triangulo + circulo
    return total
#proceso
print ("Area de la figura")
radio = int(input("Medida radio: "))
hipotenusa = int(input("Medida hipotenusa: "))

#output

print (f"Esta es tu area:{figura(hipotenusa,radio)}")
print ("")

print (total)
