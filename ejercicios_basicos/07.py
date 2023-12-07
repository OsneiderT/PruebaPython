# cree un programa que la recibir como dato dos numeros enteros, calcule la suma, resta y multiplicacion de dichos numeros.

# presentacion del programa
print("\n--- PROGRAMA 07 ---\n")

# datos almacenados en variables
numero_1 = float(input("Digite el primer número: ")) 
numero_2 = float(input("Digite el siguiente número: "))

# variables que almacenaran la suma,resta y multiplicacion
suma = (numero_1 + numero_2)
resta = (numero_1 - numero_2)
multiplicacion = (numero_1 * numero_2)

# muestra de los resultados en consola
print(f'\nLa Suma entre {numero_1} y {numero_2} es: {suma}') 
print(f'\nLa Resta entre {numero_1} y {numero_2} es: {resta}') 
print(f'\nLa Multiplicaión entre {numero_1} y {numero_2} es: {multiplicacion}') 

# finalizacion del programa
print("\n--- FIN DEL PROGRAMA ---\n")