#inputs
def descuento (compra,descuento):
    promo = compra * 0.15
    total = (compra - promo)
    return total

precio = int(input("Inserta el precio de tu compra: "))

#proceso
a = descuento (precio, 0.15)
print (f"Este es el total{})
