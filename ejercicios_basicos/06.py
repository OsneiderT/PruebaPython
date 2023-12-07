# Calculadora de Descuento:
# Desarrolla un programa que pida al usuario ingresar el precio original de un producto y el porcentaje de descuento aplicado. 
# Calcula e imprime el precio final después del descuento.


# presentacion del programa en consola
print("\n--- PROGRAMA 06 ---\n")
print("-> Calculadora de Descuento.\n")

# pedir datos por consola para luego almacenar en variables 
precio_producto = float(input("Digite el precio del Producto: "))
porcentaje_descuento = float(input("\nDigite el descuento aplicado para ese producto: "))

# calculamos el descuento
descuento = precio_producto * (porcentaje_descuento / 100)
precio_final = precio_producto - descuento

# mostrar en consola el precio final del producto
print(f'\nPrecio final a pagar con el descuento aplicado es: $ {precio_final:.3f} pesos.')

# finalizacion del programa
print("\n--- FIN DEL PROGRAMA ---\n")