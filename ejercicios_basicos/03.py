# Listas:Crea una lista de números y realiza las siguientes acciones:
# Imprime la suma de todos los números.
# Imprime el número más grande de la lista.
# Imprime los números pares de la lista.

# se crea la lista se procede a mostrar al usuario y su suma se almacena en una variable
print("\n--- PROGRAMA 03 ---\n")
lista = [1, 45, 34, 68, 32, 100, 11, 9, 4]
suma = sum(lista)
print(f'La lista contiene los siguientes elementos {lista}.')

# proceder a imprimir las respectivas condiciones
print("\n--- SUMA DE LOS ELEMENTOS DE LA LISTA ---")
print(f'La suma de los elementos de la lista es: {suma}.')

# numero mayor de la lista hacindo uso del al funcion max 
print("\n--- NUMERO MAS GRANDE DE LA LISTA ---")
print(f'El número mas grande de la lista es {max(lista)}.')

# numero par o pares que se encuentren en la lista
print("\n--- NUMEROS PAR DE LA LISTA")
numeros_pares = [num for num in lista if num % 2 == 0]
print(f'El número par o los números pares de la lista es: {numeros_pares}.')

print("\n--- FIN DEL PROGRAMA ---\n")

