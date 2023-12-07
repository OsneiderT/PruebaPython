# construir un programa que al recibir como dato el radio de un circulo, calcule e imprima tanto su area como la longitud de su circunferencia

# el area de un circulo la calculamos como:
# area = π * radio ** 2

# la circunferencia del circulo la calculamos de la siguiente manera:
# longitud de la circunferencia: 2 * π * radio


# presentacion del programa
print("\n--- PROGRAMA 09 ---\n")
print("El programa recibira el radio del circulo, y calculara su Area y la Longitud de su Circunferencia.")

# variables y almacenacion de datos
radio_circulo = float(input("\n--> Digite el radio del circulo: "))
pi = 3.14159265359
area = (pi * radio_circulo ** 2)
longitud_circunferencia = (2 * pi * radio_circulo)

# presentacion de los datos en consola
print(f'\nEl Area del circulo es: {area:.1f}')
print(f'La Longitud de la Circunferencia del Circulo es: {longitud_circunferencia:.1f}')

# finalizacion del programa
print("\n--- FIN DEL PROGRAMA ---\n")