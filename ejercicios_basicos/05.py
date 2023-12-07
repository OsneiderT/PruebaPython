# Conversor de Temperatura:
# Desarrolla un programa que convierta la temperatura de grados Celsius a grados Fahrenheit. 
# Solicita al usuario que ingrese la temperatura en Celsius y muestra el resultado en Fahrenheit.


# entrada al programa
print("\n--- PROGRAMA 05 ---\n")
print("-> Programa que convierte la temperatura de grados Celsius a grados Fahrenheit.")

# pedir datos al usuario en consola
celsius = float(input("\n-> INGRESE LA TEMPERATURA EN GRADOS CELSIUS: "))

# convertir los grados celsius a Fahrenheit
celsius_conver = (celsius * 9/5) + 32

# mostrar en la consola al usuario
print(f'\n-> La temperatura ingresada a grados Fahrenheit es: {celsius_conver}°F')

# mensaje final del programa
print("\n--- FIN DEL PROGRAMA ---\n") 