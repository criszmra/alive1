
#inputs
print ("Descuentos")
cantidad = int(input("Cuantos productos vas a comprar? "))
precio = int(input("Cual es el precio del producto? "))

#proceso
total = cantidad * precio
if total >= 5000:
    desc = total * 0.15
    total1 = (total - desc)
    print (f"Este es el precio con descuento: {total1}")
elif total >= 3000:
    desc1 = total * 0.10
    total2 = (total - desc1)
    print (f"Este es el precio con descuento: {total2}")
else:
    print ("No entra en descuento")
