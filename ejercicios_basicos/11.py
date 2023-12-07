# construir un programa que calcule e imprima el numero de segundos que hay en un determinado numero de dias.
# dato: dia (variable de tipo entero que representa el numero de dias)

# presentacion del programa
print("\n--- PROGRAMA 11 ---\n")
print("El programa dependiendo del numero de dias que ingrese, calculara el numero de segundos en el determinado numero de dias.")

# variables para el dia y calcular los segundos
dia = int(input("\nDigite el numero de dias: "))
segundos_1dia = 86.400
segundos = segundos_1dia * dia

# muestra en consola de los resultados
print(f'\nPara {dia} dias, hay {segundos:.3f} segundos.')

# finalizacion del programa
print("\n--- FIN DEL PROGRAMA ---\n")