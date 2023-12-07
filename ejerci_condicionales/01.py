# construye un programa que, al recibir como dato el salario de un profesor de una universidad, calcule 
# el incremento del salario de acuerdo con el siguiente criterio y escriba el nuevo salario del profesor.

# salario < $18.000 -> incremento del 12%
# $18.000 <= salario <= 30.000 -> incremento del 8%
# 30.000 < salario <= $50.000 -> incremento del 7%
# 50.000 < salario -> incremento del 6%

# presentacion del programa
print("\n--- PROGRAMA 01 ---\n")
print("El programa recibira como dato el salario de un profesor y de acuerdo a su salario se hara su respectivo incremento de salario.")

# recibir datos por caonsola almacenado en variable
salario_profesor = float(input("\nPor favor digite su salario: "))

# condiciones del programa de acuerdo al salario ingresado
if salario_profesor < 18.000:
    salario_nuevo = salario_profesor + (salario_profesor * 0.12)
    print(f'\nSu salario es de ${salario_profesor:.3f} pesos. El incremento para su salario es del 12%, por consiguiente su salario sera de ${salario_nuevo:.3f} pesos.')

elif 18.000 <= salario_profesor <= 30.000:
    salario_nuevo = salario_profesor + (salario_profesor * 0.8)
    print(f'\nSu salario es de ${salario_profesor:.3f} pesos. El incremento para su salario es del 8%, por consiguiente su salario sera de ${salario_nuevo:.3f} pesos.')
    
elif 30.000 < salario_profesor <= 50.000:
    salario_nuevo = salario_profesor + (salario_profesor * 0.7)
    print(f'\nSu salario es de ${salario_profesor:.3f} pesos. El incremento para su salario es del 7%, por consiguiente su salario sera de ${salario_nuevo:.3f} pesos.')

else:
    salario_nuevo = salario_profesor + (salario_profesor * 0.6)
    print(f'\nSu salario es de ${salario_profesor:.3f} pesos. El incremento para su salario es del 6%, por consiguiente su salario sera de ${salario_nuevo:.3f} pesos')


# finalizacion del programa
print("\n--- FIN DEL PROGRAMA ---\n")