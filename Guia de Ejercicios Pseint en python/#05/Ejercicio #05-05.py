# Usando cualquier condicional:
# ● (1) Solicitá el ingreso de un día y un mes del año.
# ● (2) Según la fecha ingresada, mostrá por pantalla un mensaje que indique si corresponde al
# Verano, Otoño, Invierno o Primavera.

def determinar_estacion(mes):
    if mes in (1, 2, 12):
        return "Verano"
    elif mes in (3, 4, 5):
        return "Otoño"
    elif mes in (6, 7, 8):
        return "Invierno"
    elif mes in (9, 10, 11):
        return "Primavera"
    else:
        return "Mes inválido"
    
# Solicita al usuario ingresar un número de mes (1-12)
try:
    numero_mes = int(input("Ingresa el número de mes (1-12): "))
    estacion = determinar_estacion(numero_mes)
    print(f"La estación correspondiente al mes {numero_mes} es: {estacion}")
except ValueError:
    print("Ingresa un número válido.")