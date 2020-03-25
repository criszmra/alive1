
#inputs
print ("la calificación mexicana a una calificación en USA")
cal = int(input("Inserta calificacion del alumno"))

#proceso
if cal > 9:
    print ("Calificacion equivale a: A+")
elif cal >= 8 and cal <= 9:
    print ("Calificacion equivale a: A")
elif cal < 8 and cal >= 7:
    print ("Calificacion equivale a: B")
elif cal < 7 and cal >= 6:
    print ("Calificacion equivale a: C")
else:
    print ("Calificacion equivale a: D")
