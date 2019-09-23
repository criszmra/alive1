#inputs

print ("Ahorro quincenal")
sueldo = int(input("Cual es su sueldo mensual?: "))

#proceso
ahorro = sueldo * 0.15
total = sueldo - ahorro
total2 = total * 12
print (f"Este es el total ahorrado: {total2}")
