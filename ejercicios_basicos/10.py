# construir u programa que al recibir una cantidad expresada en dolares, convierta esa cantidad en pesos colombianos a demas de preguntar al usuario
# el precio actual del dolar

# presentacion del programa
print("\n--- PROGRAMA 10 ---\n")
print("El programa recibira una cantidad en dolares y se hara la conversion a pesos colombianos.")

# variables y conversion de dolar a pesos colombianos
precio_dolar = float(input("\nDigite el precio actual del dolar: "))
dolares_a_convertir = float(input("Digite la cantidad de dolares a convertir: "))
pesos_colombianos = dolares_a_convertir * precio_dolar

# muestra de resultados por consola al usuario
print(f'\nLos dolares que usted ingreso son ${dolares_a_convertir} dolares, en Pesos colombianos son: ${pesos_colombianos:.3f} pesos.')

# finalizacion del programa
print("\n--- FIN DEL PROGRAMA ---\n") 