
#inputs
def terreno (a,b,c):
    area1 = a/2 * b/2
    area2 = b * c

    total = area1 + area2
    return total

#proceso

print ("Sacar el area del terreno")
ladoa = int(input("Insertar medida de lado a: "))
ladob = int(input("Inserta medida de lado b: "))
ladoc = int(input("Inserta medida de lado c: "))

print (f"Esta es tu area:{terreno(ladoa,ladob,ladoc)}")
print ("")
