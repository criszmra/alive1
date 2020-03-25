#inputs
def ahorro (sueldo,descuento):
    ahorro1 = sueldo * descuento
    total = sueldo - ahorro1
    total2 = total * 12
    return total2

#proceso
print ("Ahorro quincenal")
paga = int(input("Cual es su sueldo mensual?: "))

#proceso
a = ahorro (paga, 0.15)
print (f"Este es el total ahorrado:{a}")
