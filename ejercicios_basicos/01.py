# Condicionales:Crea un programa que pida al usuario ingresar un número. Luego, verifica si ese número es positivo, 
# negativo o cero, e imprime un mensaje correspondiente.

# pedir numro por consola al usuario
print("\n--- PROGRAMA 01 ---\n")
numero = int(input("Digite un número ya sea positivo o negatico: "))

# establecer las condiciones que toma el programa de acuerdo al numero ingresado
if numero > 0:
    print(f'\nEl número ingresado {numero}, es POSITIVO.')
    
elif numero == 0:
    print(f'\nEl número ingresado {numero}, es NEUTRO.')
    
else:
    print(f'\nEl número ingresado {numero}, es NEGATIVO.')

print("\n--- FIN DEL PROGRAMA ---\n")