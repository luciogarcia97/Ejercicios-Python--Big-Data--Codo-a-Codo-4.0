# Usando Leer:
# ● (1) Solicitá los ingresos por teclado del año de nacimiento de una persona y del año actual (usá
# mensajes de ayuda para hacer más fácil ambos ingresos).
# ● (2) Calculá la edad actual de la persona.
# ● (3) Dejá una línea en blanco en la pantalla.
# ● (4) Mostrá un mensaje por pantalla que informa el dato calculado en (2) (aclará los datos
# mostrados)
año_nacimiento = input("Ingresa el año de tu nacimiento: ")
año_actual = input("Ingresa el año actual: ")

edad = int(año_actual) - int(año_nacimiento)

print("")
print("Año de tu nacimiento:", str(año_nacimiento))
print("Año actual:", str(año_actual))
print("Edad:", str(edad))
