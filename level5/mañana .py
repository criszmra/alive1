
#inputs
print ("Inserta las siguiente cantidades en numeros: ")
dia = int(input("Que dia es hoy: "))
mes = int(input("Que mes es hoy: "))

#proceso
if dia < 30 and mes <= 12:
    dia2 = dia + 1

    print (f"Mañana es: {dia2}")
    print (f"Del mes: {mes}")
elif dia == 30 and mes <= 11:
    dia = dia - 29
    print (f"Mañana es: {dia}")
    mes1 = mes + 1
    print (f"Del mes: {mes1}")
elif dia == 30 and mes == 12:
    dia1 = dia - 29
    mes2 = 12 - 11
    print (f"Mañana es: {dia1}")
    print (f"Mañana es: {mes2}")
else:
    print ("Hay algun dato incorrecto")
