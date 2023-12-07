# en una tienda departamental ofrecen descuentos a los clientes en la navidad, de acuerdo con el monto de su compra.
# el criterio para establecer el descuento se muestra abajo.
# construya un programa que, al recibir como dato el monto de la compra del cliente, obtenga el precio real que debe pagar
# luego de aplicar el descuento correspondiente.

# compra < $800 -> descuento 0%
# $800 <= compra <= $1500 -> descuento 10%
# 1500 < compra <= $5000 -> descuento 15%
# $5000 < compra -> descuento 20% 


# inicializacion del programa
print("\n--- PROGRAMA 04 ---\n")
print("El programa determinara cua es el precio a pagar despues de aplicar el descuento correspondiente.")


# monto de la compra en una variabe
monto_compra = float(input("\nDigite el precio del producto a comprar: "))

# decicion del programa
if monto_compra < 800:
    print(f'\nEl precio final es: ${monto_compra} pesos, no aplica descuento.')

elif 800 <= monto_compra <= 1500:
    monto_compra -= (monto_compra * 0.10)
    print(f'\nEl precio final con el descuento aplicado que es del 10% es: ${monto_compra} pesos.')

elif 1500 < monto_compra <= 5000:
    monto_compra -= (monto_compra * 0.15)
    print(f'\nEl precio final con el descuento aplicado que es del 15% es: ${monto_compra} pesos.')
    
else:
    monto_compra -= (monto_compra * 0.20)
    print(f'\nEl precio final con el descuento apicado es del 20% es: ${monto_compra} pesos.')


# fianlizacion del programa
print("\n--- FIN DEL PROGRAMA ---\n")