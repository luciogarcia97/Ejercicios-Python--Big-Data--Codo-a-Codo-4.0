# ● (1) Vamos a suponer que todas las personas se jubilan a los 65 años.
# ● (2) El programa debe borrar la pantalla y mostrar un mensaje subrayado a modo de título,
# explicando que tarea resuelve (título breve).
# ● (3) El programa debe solicitar el ingreso de 3 datos: nombre, edad y año actual.
# Los ingresos de datos deben estar bien explicados con mensajes.
# ● (4) Con los datos ingresados calculá y guardá el año de jubilación de la persona.
# ● (5) Dejá una línea en blanco para separar de los ingresos.
# ● (6) Mostrá la información obtenida de modo que quede similar al siguiente ejemplo :

# Jose se jubila en el año 2034

import os

edad_jubilacion = 65

os.system('cls' if os.name == 'nt' else 'clear')
print("Informacion Jubilatoria")
print("-----------------------")

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
año_actual = int(input("Ingrese el año actual: "))

año_jubilacion = (edad_jubilacion - edad)  + año_actual

print("")

print(nombre + " se jubila en el año " + str(año_jubilacion - 1))