# Usando Condicionales Completos:
# ● (1) Ingresá por teclado el precio de un producto.
# ● (2) Ingresá por teclado el dinero que tenes disponible.
# ● (3) Decidí e indicá con un mensaje en pantalla si el dinero es suficiente para comprar el producto o
# si el dinero no es suficiente para la compra.

precio = float(input("Ingresa el precio del producto: "))
dinero = float(input("Ingresa el dinero que tenes disponible: "))

print("")

if dinero >= precio:
    print("Te alcanza para comprar")
else:
    print("No te alcanza para comprar")
