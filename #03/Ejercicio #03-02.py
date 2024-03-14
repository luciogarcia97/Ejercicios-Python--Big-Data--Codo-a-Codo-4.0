# ● (1) Mostrá un mensaje por pantalla con el cartelito:
# +-----------+
# | Clase #02 |
# +-----------+
# Presione una tecla para continuar ...
# ● (2) Programá una espera de teclado.
# ● (3) Programá limpiar la pantalla y luego mostrá un mensaje:
# Gracias por su colaboración.
import msvcrt #Uso una biblioteca para poder usar el comando de presskey
print("+-----------+")
print("| Clase #02 |")
print("+-----------+")
print("Presione una tecla para continuar ...")

msvcrt.getch() #press any key

print("Gracias por su colaboración.")