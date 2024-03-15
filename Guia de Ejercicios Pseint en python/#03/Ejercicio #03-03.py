# ● (1) Mostrá un mensaje por pantalla con el cartelito:
# +-----------+
# | Clase #02 |
# +-----------+
# ● (2) Solicitá el ingreso de una cantidad de segundos (usá un mensaje de ayuda).
# ● (3) Mostrá un mensaje "Esperando X segundos", donde X sea la cantidad ingresada.
# ● (4) Programá una espera de tiempo de la cantidad de segundos ingresada.
# ● (5) Programá limpiar la pantalla y luego mostrá un mensaje:
# Gracias por su colaboración.

import time
import os

print("+-----------+")
print("| Clase #02 |")
print("+-----------+")

numero = input("Ingresa la cantidad de segundos: ")
print("Esperando " + str(numero) + " segundos")

time.sleep(int(numero))

os.system('cls' if os.name == 'nt' else 'clear')

print("Gracias por su colaboración.")