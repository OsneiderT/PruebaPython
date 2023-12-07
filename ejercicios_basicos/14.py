# construir un programa que al recibir como dato el radio de una esfera, calcule e imprima el area y su volumen

# el area de la esfera se calcula: 4 * pi * radio**2 
# el volumen se calcula: 1 / 3 * pi * radio **3

import math

# presentacion del programa
print("\n--- PROGRAMA 14 ---\n")
print("El programa recibira como dato el radio de una esfera y calculara el Area y su Volumen.")

# variable para recibir dato y la formulas
radio_esfera = float(input("\nDigite el radio de la esfera: "))
area_esfera = 4 * math.pi * pow(radio_esfera, 2)
volumen_esfera = 1 / 3 * math.pi * pow(radio_esfera, 3)

# presentacion por consola de los resultados
print(f'\nEl Area de la esfera es: {area_esfera:.1f}')
print(f'El Volumen de la esfera es: {volumen_esfera:.1f}')

# finalizacion del programa
print("\n--- FIN DEL PROGRAMA ---\n")