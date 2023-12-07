# escribe un programa que al recibir como dato un numero de cuatro digitos genere una impresion como esta
# numero: 6352
# impresion: 
# 6
# 3
# 5
# 2


# presentacion del programa
print("\n--- PROGRAMA 12 ---\n")
print("El programa recibira un numero de 4 digitos y los imprimira por separado cada digito.")

# variable para almacenar el numero
numero = input("\nDigite un numero que contenga 4 digitos: ")

# muestra en consola
print(f'\nEl numero ingresado es {numero} sus digitos separados son:\n\nPrimer digito: {numero[0]}\nSegundo digito: {numero[1]}\nTercer digito: {numero[2]}\nCuarto digito: {numero[3]}')

# finalizacion del programa
print("\n--- FIN DEL PROGRAMA ---\n")