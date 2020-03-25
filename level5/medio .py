
#inputs
n1 = int(input("Dame tu primer numero entero: " ))
n2 = int(input("Dame tu segundo numero entero: " ))
n3 = int(input("Dame tu tercer numero entero: " ))

#proceso
if n2 < n1 < n3:
    print ("El numero 1 es el numero de en medio")
elif n1 < n2 < n3:
    print ("El numero 2 es el numero de en medio")
else:
    print ("El numero 3 es el numero de en medio")
