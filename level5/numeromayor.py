
#inputs
print ("Numero mayor")
numero1 = float(input("Dame tu primer numero"))
numero2 = float(input("Dame tu segundo numero"))
numero3 = float(input("Dame tu tercer numero"))

#proceso

if numero1 > numero2 and numero1 > numero3:
    print ("Numero 1 es el mayor")
elif numero2 > numero3 and  numero2 > numero1:
    print ("Numero 2 es el mayor")
elif numero3 > numero2 and numero3 > numero1:

    print ("Numero 3 es el mayor")
