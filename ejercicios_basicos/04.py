# se necesita crear una aplicación que permita calcular el perimetro y area de las siguientes figuras
# triangulo
# paralelogramo
# cuadrado
# rectángulo
# rombo
# trapecio
# poligono regular
# círculo


# inicio del programa
print("\n--- PROGRAMA 04 ---")

# presentacion del menu al usuario
print("\nSeleccione una de las siguientes figuras para calcular su AREA y PERIMETRO")
print("\n1. Triangulo")
print("2. Paralelogramo")
print("3. Cuadrado")
print("4. Rectángulo")
print("5. Rombo")
print("6. Trapecio")
print("7. Círculo")

# variable que contiene la opcion seleccionada
opcion = int(input("\nSeleccione un número de opción: "))

# establecer las condiciones que debe tomar el programa de acuerdo a la opcion seleccionada
match opcion:
    case 1: # caso triangulo
        # perimetro
        print("Opcion elegida TRIANGULO.")
        print("\nPor favor digite el Perimetro del TRIANGULO.")
        tri_a = float(input("A: "))
        tri_b = float(input("B: "))
        tri_c = float(input("C: "))
        perimetro_tri = (tri_a + tri_b + tri_c) # formula para hallar el perimetro del triangulo
        print(f'\nEl PERIMETRO del TRIANGULO es: {perimetro_tri:.1f} cm.')
        
        # area
        print("\nPor favor digite el Area del TRIANGULO.")
        base_tri = float(input("BASE: "))
        altura_tri = float(input("ALTURA: "))
        area_tri = (base_tri * altura_tri) / 2 # formula para hallar eel area del triangulo
        print(f'\nEl AREA del TRIANGULO es: {area_tri:.1f} cm.')
    
    case 2: # caso paralelogramo
        # perimetro
        print("Opción elegida PARALELOGRAMO.")
        print("\nPor favor digite el Perimetro del PARALELOGRAMO.")
        parale_b = float(input("B: "))
        parale_a = float(input("A: "))
        perimetro_parale = 2*(parale_b) + 2*(parale_a) # formula para hallar el perimetro del paralelogramo
        print(f'\nEl PERIMETRO del PARALELOGRAMO es: {perimetro_parale:.1f} cm.')
        
        # area
        print("\nPor favor digite el Area del PARALELOGRAMO.")
        base_parale = float(input("BASE: "))
        altura_parale = float(input("ALTURA: "))
        area_parale = base_parale * altura_parale # formula para hallar el area del paralelogramo
        print(f'\nEl AREA del PARALELOGRAMO es: {area_parale:.1f} cm.')
    
    case 3: # caso cuadrado
        # perimetro
        print("Opcion elegida CUADRADO.")
        print("\nPor favor digite el Perimetro del CUADRADO.")
        lados_cuad = float(input("A: "))
        perimetro_cuad = 4 *(lados_cuad) # formula para hallar el perimetro del cuadrado
        print(f'\nEl PERIMETRO del CUADRADO es: {perimetro_cuad:.1f} cm.')
        
        # area
        print("\nPor favor digite el Area del CUADRADO.")
        lado_cuadra = float(input("A: "))
        area_cuadra = lado_cuadra ** 2 # formula para hallar el area del cuadrado
        print(f'\nEl AREA del CUADRADO es: {area_cuadra:.1f} cm.')
        
    case 4: # caso rectangulo
        # perimetro
        print("Opcion elegida RECTANGULO.")
        print("\nPor favor digite el Perimetro del RECTANGULO.")
        rect_b = float(input("B: "))
        rect_a = float(input("A: "))
        perimetro_rect = 2*(rect_b) + 2*(rect_a) # formula para hallar el perimetro del rectangulo
        print(f'\nEl PERIMETRO del RECTANGULO es: {perimetro_rect:.1f} cm.')
        
        # area
        print("\nPor favor digite el Area del RECTANGULO.")
        base_rect = float(input("BASE: "))
        altura_rect = float(input("ALTURA: "))
        area_rect = base_rect * altura_rect # formula para hallar el area del rectangulo
        print(f'\nEl AREA del RECTANGULO es: {area_rect:.1f} cm.')
        
    case 5: # caso rombo
        # perimetro
        print("Opcion elegida ROMBO.")
        print("\nPor favor digite el Perimetro del ROMBO.")
        lados_rom = float(input("A: "))
        perimetro_rom = lados_rom ** 4 # formula para hallar el perimetro del rombo
        print(f'\nEl PERIMETRO del ROMBO es: {perimetro_rom:.1f} cm.')
        
        # area
        print("\nPor favor digite el Area del ROMBO.")
        dia_a = float(input("A: "))
        dia_b = float(input("B: "))
        area_rom = (dia_a * dia_b) / 2 # formula para hallar el area del rombo
        print(f'\nEl AREA del ROMBO es: {area_rom:.1f} cm.')
        
    case 6: # caso trapecio
        # perimetro
        print("Opcion elegida TRAPECIO.")
        print("\nPor favor digite el Perimetro del TRAPECIO.")
        base_menor = float(input("base menor: ")) #  base menor
        base_mayor = float(input("BASE MAYOR: ")) # base mayor
        trape_a = float(input("A: "))
        trape_c = float(input("C: "))
        perimetro_trapec = (trape_a + base_menor + trape_c + base_mayor) # formula para hallar el perimetro del trapecio
        print(f'\nEl PERIMETRO del TRAPECIO es: {perimetro_trapec:.1f} cm.')
        
        # area
        print(f'\nPara hallar el Area del TRAPECIO se tomaron los sigueintes datos de la BASE MAYOR que es, {base_mayor} y la base menor que es, {base_menor}.')
        print("Solo digite la altura del TRAPECIO.")
        altura = float(input("Altura: "))
        area_trape = (base_mayor + base_menor) * altura / 2 # formula para hallar el area del trapecio
        print(f'\nEl AREA del TRAPECIO es: {area_trape:.1f} cm.')
        
    case 7: # caso circulo
        # perimetro
        print("Opcion elegida CIRCULO.")
        print("\nPor favor digite el Perimetro del CIRCULO.")
        pi = 3.14159
        radio = float(input("RADIO: "))
        perimetro_circ = (2 * pi * radio) # formula para hallar el perimetro del circulo
        print(f'\nEl PERIMETRO de CIRCULO es: {perimetro_circ:.1f} cm.')
        
        # area
        print(f'Para hallar el AREA del circulo tomare en cuenta PI que es, {pi} y el radio que es, {radio}.')
        area_circulo = pi * radio ** 2 # formula para hallar el area del circulo
        print(f'\nEl AREA del CIRCULO es: {area_circulo:.1f} cm.')
    
    case _: # caso por defecto si introduce una opcion no establecida en el programa
        print("\nOpcion no valida por favor digite una de las opciones establecidas anteriormente.")
        
        
# finalizacion del programa
print("\n--- FIN DEL PROGRAMA\n")