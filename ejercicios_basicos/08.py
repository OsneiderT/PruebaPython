# construye un programa que al recibir como datos el costo de un articulo vendido y la cantidad de dinero entregada por el cliente calcule e imprima

# 1. el cambio que se debe entregar al cliente, si el pago efectuado es mayor que el precio del producto.
# 2. que pasa si el cliente paga exactamente lo que vale el producto.
# 3. la cantidad de dinero que falta por pagar, si el pago efectuado es menor que el precio del producto. 

# presentacion del programa
print("\n--- PROGRAMA 08 ---")

# variables para almacenar costo articulo, y dinero cleinte
print("\nEn las respectivas casillas digite el costo del articulo a comprar, y el dinero que tienes respectivamente.\n")
costo_articulo =  float(input("Costo del articulo: "))
dinero_cliente = float(input("Cantidad de dinero: "))

# condiciones que debe tomar el programa

# condicion 1
if costo_articulo < dinero_cliente:
    cambio = dinero_cliente - costo_articulo
    print(f'\nSu cambio es: ${cambio:.3f} pesos.')

# condicion 2
elif costo_articulo == dinero_cliente:
    print(f'\nPago realizado con exito.')
    
# condicion 3
elif costo_articulo > dinero_cliente:
    faltante = costo_articulo - dinero_cliente
    print(f'\nTienes ${dinero_cliente:.3f} pesos, el producto vale ${costo_articulo:.3f} pesos. Te faltan ${faltante:.3f} pesos.')
    

# finalizacion del programa
print("\n--- FIN DEL PROGRAMA ---\n")