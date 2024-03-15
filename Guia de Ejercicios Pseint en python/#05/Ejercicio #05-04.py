# Usando condicionales:
# ● (1) Solicitá el número de mes del año.
# ● (2) Según lo ingresado, informá por pantalla la cantidad de días que tiene ese mes (suponemos año
# no-bisiesto)

mes = int(input("Ingresa el mes: "))
anio = int(input("Ingresa el año: "))

if mes in (1,3,5,7,8,10,12):
    print("Este mes cuenta cuenta con 31 dias")
elif mes in (4,6,9,11):
    print("Este mes cuenta cuenta con 30 dias")
else:
    print("Este mes cuenta cuenta con 28 dias")

