# Usando Condicional Simple:
# ● (1) Ingresa por teclado la nota de un examen de una materia (usa un mensaje de aclaración).
# ● (2) Sabiendo que la materia se aprueba con una nota mínima de 4, indicá con un mensaje por
# pantalla únicamente si el examen está APROBADO.

nota = int(input("Ingresa la nota correspondiente: "))

if nota >= 4:
    print("Aprobado")