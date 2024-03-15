# Usando condicionales, operadores relacionales y lógicos:
# ● (1) Solicitar el ingreso de la edad y el sexo de una persona.
# ● (2) Suponiendo que las mujeres pueden jubilarse a los 60 años y los varones a los 65 años, mostrá
# por pantalla algunos de los 2 mensajes siguientes, según corresponda:
# La persona aún no se puede jubilar.
# La persona ya se puede jubilar.

edad =  int(input("Ingrese su edad: "))
sexo =  int(input("Ingrese su sexo [M=0/F=1]: "))

if (edad >= 60) & (sexo):
    print("La persona se puede jubilar")
elif (edad >= 65) & (not sexo):
    print("La persona se puede jubilar")
else:
    print("La persona aun no se puede jubilar")

    