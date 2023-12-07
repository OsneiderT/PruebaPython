# construye un programa que determine, al recibir como datos dos numeros enteros,
# si un numero es divisor de otro.

# inicializacion del programa
print("\n--- PROGRAMA 02 ---\n")
print("El programa recibira dos numeros y determinara si un número es divisor de otro.")

# variable para recibir los dos numero
numero_1 = int(input("\nDigite el primer número: "))
numero_2 = int(input("Digite el segundo número: "))

# condiciones del programa
if numero_1 % numero_2 == 0:
    print(f'\nEl número {numero_2} es divisor de {numero_1}.')

else:
    print(f'\nEl número {numero_2} no es divisor de {numero_1}.')


# finalizacion del programa
print("\n--- FIN DEL PROGRAMA ---\n")