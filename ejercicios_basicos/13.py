# construir un programa que al recibir como datos el radio, la generatriz y la altura de un cono, calcule e imprima el area de la base el area lateral
# el area total del cono y su volumen
# datos: rad, alt, gene

# area de la base se calcula: pi * radio **2
# area lateral se calcula: pi * radio * gene
# area total se calcula : AB + AL
# el volumen se calcula: (1 / 3) * AB * alt

import math

# presentacion del programa
print("\n--- PROGRAMA 13 ---\n")
print("El programa pedira unos datos y calculara, el Area de la base, el Area lateral, el Area total del cono y su volumen.")

# variables para los datos
radio = float(input("\nDigite el radio del cono: "))
altura = float(input("Digite la altura del cono: "))
generatriz = float(input("Digite la generatriz del cono: "))

# formulas para resolver el problema
area_base = math.pi * pow(radio, 2)
area_lateral = math.pi * radio * generatriz
area_total = area_base + area_lateral
volumen = (area_base * altura) / 3

# presentar en consola los datos
print(f'\n->El Area de la base del cono es: {area_base:.1f}')
print(f'->El Area lateral del cono es: {area_lateral:.1f}')
print(f'->El Area total del cono es: {area_total:.1f}')
print(f'->El Volumen del cono es: {volumen:.1f}')

# finalizacion del programa
print("\n--- FIN DEL PROGRAMA ---\n")