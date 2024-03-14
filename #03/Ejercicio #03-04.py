# Usando Leer y operaciones aritméticas:
# ● (1) Solicitá los ingresos por teclado de 3 notas numéricas enteras (usá mensajes de ayuda para
# hacer más fácil los ingresos).
# ● (2) Calcula el promedio de las 3 notas.
# ● (3) Dejá una línea en blanco en la pantalla.
# ● (4) Mostrá un mensaje por pantalla que informe el dato calculado en (2) (aclará los datos
# mostrados).

nota_1 = int(input("Ingresa la primera nota: "))
nota_2 = int(input("Ingresa la primera nota: "))
nota_3 = int(input("Ingresa la primera nota: "))

nota_promedio = (nota_1 +nota_2 + nota_3) / 3
print(" ")
print("Promedio de notas: " + str(nota_promedio))