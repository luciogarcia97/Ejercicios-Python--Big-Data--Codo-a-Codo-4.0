# Usando variables lógicas y condicionales :
# ● (1) Ingresá por teclado la nota final de una materia cursada.
# ● (2) Usa dos variables lógicas o flags para guardar dos condiciones:

# reprobado: si la nota es menor que 4.
# promocionado: aprobación con promoción si la nota es 7 o mayor.

# ● (3) En base al primer flag (reprobado), mostrá por pantalla un mensaje que indique la aprobación o
# reprobación de la materia.
# ● (4) En base al segundo flag (promocionado), mostrá un mensaje por pantalla ÚNICAMENTE si la
# materia está promocionada. Si no está promocionada no muestres nada.

nota = float(input("Ingresa tu nota: "))

flag = False

if nota < 4:
    flag = False
if nota >= 7:
    flag = True

if flag == 0:
    if nota >= 4:
        print("Aprobado")
    else:
        print("Reprobado")
else:
    print("Promocionado")
