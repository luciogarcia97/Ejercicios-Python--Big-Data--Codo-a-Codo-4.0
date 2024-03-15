# ● (1) Un conductor viaja en su automóvil por una ruta y se detiene en un comercio para retirar una
# caja de insumos. Posteriormente ubica y asegura la caja en el porta-equipaje del techo del vehículo,
# y reanuda el viaje.
# ● (2) Al llegar a un cruce con otra carretera, observa que debe circular por debajo de un puente que
# tiene un cartel de advertencia indicando una altura máxima permitida para el paso.
# Si la altura total del vehículo supera esa altura máxima, no puede pasar y deberá tomar un
# desvío.
# ● (3) Teniendo en cuenta que las medidas de alturas en estos casos se expresan en metros y pueden
# tener decimales, realizá un programa que le solicite al conductor 3 datos:
# Altura del automóvil
# Altura de la caja que transporta
# Altura máxima permitida de paso (esta altura se puede alcanzar)
# ● (4) Con esos tres datos deberás primero calcular y guardar la altura total del vehículo cargado.
# ● (5) Luego decidir e indicarle al conductor con un mensaje

altura_auto = float(input("Ingrese la altura del auto: "))
altura_caja = float(input("Ingrese la altura de la caja: "))
altura_maxima_permitida = float(input("Ingrese la altura maxima permitida: "))

altura_total = altura_auto + altura_caja

print("")

if altura_total >= altura_maxima_permitida:
    print("Debe tomar un desvio")
else:
    print("Puede pasar por debajo del puente")
