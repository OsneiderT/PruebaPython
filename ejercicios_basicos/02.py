# Cadenas de Texto: Solicita al usuario que ingrese una cadena de texto. Luego, realiza las siguientes acciones:
# Imprime la longitud de la cadena.
# Imprime la cadena en mayúsculas.
# Imprime la cadena en minúsculas.


# solicitar la cadena de texto al usuario
print("\n--- PROGRAMA 02 ---\n")
texto = input('Digite una cadena de texto ya sea en minúscula o mayúscula: ')

# imprimimos por consola las condiciones de la cadena de texto ingresada
print("\n--- LONGITUD DE CARACTERES ---")
print(f"\nLa cadena de texto ingresada '{texto}', su longitud de caracteres es de: {len(texto)}.")

print("\n--- CADENA DE TEXTO EN MAYUSCULAS ---")
print(f"\nLa cadena de texto ingresada '{texto}', en mayúsculas seria: {texto.upper()}.")

print("\n--- CADENA DE TEXTO EN MINUSCULA ---")
print(f"\nLa cadena de texto ingresada '{texto}', en minúsculas seria: {texto.lower()}.\n")