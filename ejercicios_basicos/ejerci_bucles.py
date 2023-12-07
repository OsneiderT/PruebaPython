# ejercicios bucle while

# Contador Ascendente: Crea un bucle while que imprima los números del 
# 1 al 5 en orden ascendente.
'''
contador = 1
while contador <= 5:
    print(contador)
    contador += 1
print('ejecucion terminada')



# Suma Acumulativa: Utiliza un bucle while para calcular 
# la suma acumulativa de los primeros 10 números naturales (1 + 2 + 3 + ... + 10).

numero = 1
suma = 0

while numero <= 10:
    suma += numero
    numero += 1
print(f'la suma acumulativa de los 10 primeros numeros es: {suma}')


# Adivina el Número: Escribe un programa que le pida al usuario 
# adivinar un número secreto. El programa debe seguir pidiendo al 
# usuario que ingrese un número hasta que adivinen el número correcto.

while True:
    numero_secreto = 11
    numero_user = int(input('Trata de adivinar el número: '))
    
    if numero_user == numero_secreto:
        print(f'felicidades el numero secreto es {numero_secreto}, y tu digitaste el, {numero_user}')
        break
    else:
        print('Sigue intentandolo')
        
'''

# ejercicios bucle for

# Imprimir Elementos de una Lista: Utiliza un bucle for para imprimir 
# cada elemento de una lista de frutas. Puedes crear tu propia 
# lista de frutas.

frutas = ['manzana', 'pera', 'mora', 'fresa', 'papaya']

for i in frutas:
    print(f'Las frutas son: {i}')



# Tabla de Multiplicar: Crea un bucle for que imprima la tabla de 
# multiplicar del 5 (5, 10, 15, ..., 50).

tabla = 5
for numero in range(1, 11):
    resultado = (tabla * numero)
    print(f'{tabla} x {numero} = {resultado}')
    
    


# Suma de Números Pares: Escribe un programa que sume todos los números 
# pares del 1 al 20 utilizando un bucle for.

suma_pares = 0

for numero in range(2, 21, 2):
    suma_pares += numero

print("La suma de los números pares del 1 al 20 es:", suma_pares)




