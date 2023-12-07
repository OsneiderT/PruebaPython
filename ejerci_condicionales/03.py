# construir un programa que, al recibir como datos de entrada tres valores enteros diferentes entre si,
# determine si los mismos estan en orden creciente


# inicializacion del programa
print("\n--- PROGRAMA 03 ---\n")
print("El programa pedira 3 digitos y determinara si estan en orden creciente.")


# Pedir datos en consola
numero_1 = int(input("\nDigite el primer número: "))
numero_2 = int(input("\nDigite el segundo número: "))
numero_3 = int(input("\nDigite el tercer número: "))

# condiciones del programa
if numero_1 < numero_2 < numero_3:
    print("\nLos números estan ordenados de forma creciente.")

else:
    print("\nLos números no estan ordenados de forma creciente.")

# finalizacion del programa
print("\n--- FIN DEL PROGRAMA ---\n")