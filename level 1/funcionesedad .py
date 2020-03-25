#inputs
def edades (actual,nacimiento):
    edad1 = actual - nacimiento
    return edad


actual = int(input("Inserta el año en el que estamos: "))
fecha = int(input("Inserta tu año de nacimiento: "))

#proceso
a = edades (actual,fecha)

print (f"Esta es tu edad: {edades(actual,fecha)}")
print ("")
b = años (2020,1999)
print(f"Esta es tu edad: {b}")
