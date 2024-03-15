# Usando condicionales, operadores relacionales y lógicos:
# ● (1) Mejorá el ejercicio anterior.
# Además de la altura, se debe solicitar la edad.
# ● (2) Solamente pueden ingresar quienes cumplan la condición de altura y tengan como máximo 10
# años de edad.

altura = float(input("Ingresa la altura: "))
edad = int(input("Ingresa la edad: "))

if (altura >= 80) & (altura <= 110) & (edad <= 10):
    print("Se le permite el ingreso.")
else:
    print("No se le permite el ingreso.")