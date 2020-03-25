
#inputs
print ("Resta absoluta: de números enteros positivos o negativos")
n1 = int(input("Inserte su primer numero"))
if n1 < 0:
   p1 = n1 * -1
n2 = int(input("Inserte su segundo numero"))
if n2 < 0:
   p2 = n2 * -1
abs (n1)
abs (n2)
#proceso

if n1 > n2:
    valor1 = n1 - n2
    print (valor1)
elif n2 > n1:
    valor2 = n2 - n1
    print (valor2)
elif p1 > n2:
    valor3 = p1 - p2
    print (valor3)
elif p2 > n1:
    valor4 = p2 - p1
    print (valor4)
