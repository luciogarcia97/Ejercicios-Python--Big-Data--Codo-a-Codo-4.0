# Usando Leer y operaciones de texto:
# ● (1) Solicitá los ingresos por teclado del primer nombre y del primer apellido de una persona (usá
# mensajes de ayuda para hacer más fácil ambos ingresos).
# ● (2) En otra variable guardá el apellido seguido de una coma, un espacio y luego el nombre.
# ● (3) Calcula la cantidad de letras de lo obtenido en [2]
# ● (4) Dejá una línea en blanco en la pantalla.
# ● (5) Mostrá un mensaje por pantalla informando:
# Registrado en la base de datos como:
# dato obtenido en punto [2]
# Nuevo registro con dato calculado en punto [3] caracteres.

primer_nombre = input("Ingresa tu primer nombre: ")
primer_apellido = input("Ingresa tu primer apellido: ")

nombre = primer_apellido + ", " + primer_nombre

cantidad_letras = len(nombre)

print("")

print("Registrado en la base de datos como:")
print(nombre)
print("Nuevo registro con " + str(cantidad_letras) + " caracteres.")