# ● (1) Un docente ingresa por teclado las 3 notas de un alumno (notas enteras), y la aprobación de los
# trabajos prácticos de la materia (S si están aprobados, N si no están aprobados).
# ● (2) El programa debe calcular el promedio de las notas y establecer el valor de una variable estado,
# de forma que contenga alguno de los 4 valores siguientes, según sea el promedio y los TPs del
# alumno:
#     "R" - Si el promedio es menor que 4
#     "D" - Si no tiene aprobados los TPs y el promedio es mayor o igual a 4.
#     "A" - Si tiene aprobados los TPs y el promedio es menor que 7.
#     "P" - Si tiene aprobados los TPs y el promedio es mayor o igual que 7.
# Como se puede observar, cada "estado" excluye a los anteriores.
# ● (3) Dejá una línea en blanco de separación de los ingresos.
# ● (4) Según el valor de la variable estado, mostrá por pantalla alguno de los 4 mensajes siguientes:
#     Reprobado. Debe recursar la materia.
#     Debe presentar los TPs.
#     Aprobado. Debe rendir el final.
#     Promocionado.
# ● (5) Dejá una línea en blanco al final.


nota_1 = int(input("Ingrese la primera nota: "))
nota_2 = int(input("Ingrese la segunda nota: "))
nota_3 = int(input("Ingrese la tercera nota: "))

aprobacion_tp = input("Los trabajos estan aprobados?(S/N): ")

if aprobacion_tp == "S":
    aprobo_tp = True
else:
    aprobo_tp = False

nota_promedio = (nota_1 + nota_2 + nota_3) / 3

if (aprobo_tp) & (nota_promedio >= 7):
    estado = "P"
    print("")
    print("Promocionado.")
    print("")
elif (aprobo_tp) & (nota_promedio < 7):
    estado = "A"
    print("")
    print("Aprobado. Debe rendir el final.")
    print("")
elif (aprobo_tp is False) & (nota_promedio >= 4):
    estado = "D"
    print("")
    print("Debe presentar los TPs.")
    print("")
else:
    estado = "R"
    print("")
    print("Reprobado. Debe recursar la materia.")
    print("")