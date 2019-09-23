#inputs

print ("Sacar el area del terreno")
ladoa = int(input("Insertar medida de lado a: "))
ladob = int(input("Inserta medida de lado b: "))
ladoc = int(input("Inserta medida de lado c: "))

#proceso

area1 = ladoa/2 * ladob/2

area2 = ladob * ladoc

total = area1 + area2
print (f"Esta es el area total: {total}")
