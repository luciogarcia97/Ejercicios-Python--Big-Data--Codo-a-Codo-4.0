# Usando condicionales, operadores relacionales y lógicos:
# ● (1) Solicitá el ingreso de la altura en centímetros de un niño que desea ingresar a un pelotero.
# ● (2) Según la altura se encuentre entre los 80cm y los 110cm (incluidas ambas) se le permite el
# ingreso, en caso contrario no se permite el ingreso.
# ● (3) Mostrá por pantalla un mensaje que explique ambas situaciones.


altura = float(input("Ingresa la altura: "))

if (altura >= 80) & (altura <= 110):
    print("Se le permite el ingreso.")
else:
    print("No se le permite el ingreso.")