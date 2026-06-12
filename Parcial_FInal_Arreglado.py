def valor_sillas(sillasg1, sillasvip):
    print("\n\n------- 1. VALOR SILLAS -------")
    print("1. General")
    print("2. VIP")
    print("3. Mostrar valores (Estado de sillas)")
    
    verificacion_op = False
    while verificacion_op == False:
        menu_valor_sillas = int(input("Ingresa alguna de las opciones: "))
        if menu_valor_sillas == 1 or menu_valor_sillas == 2 or menu_valor_sillas == 3:
            verificacion_op = True
        else:
            print("ERROR. Opcion no existe, intenta de nuevo.")

    if menu_valor_sillas == 1:
        print("El valor de las sillas GENERALES es de $5000")
    elif menu_valor_sillas == 2:
        print("El valor de las sillas VIP es de $10000")
    elif menu_valor_sillas == 3:
        print("\n--- Sillas Generales ---")
        for fila in sillasg1:
            print(fila)
        print("\n--- Sillas VIP ---")
        print(sillasvip)


def comprar_sillas(sillasg1, sillasvip, facturas):
    print("\n\n------- 2. COMPRAR SILLAS -------")
    
    cant_g = 0
    cant_v = 0
    total_g = 0
    total_v = 0
    
    # --- CICLO PARA SILLAS GENERALES ---
    quiere_general = input("¿Desea comprar sillas GENERALES? (s/n): ")
    while quiere_general == "s":
        sg = int(input("Digite el numero de silla GENERAL que desea: "))
        encontrado = False
        
        # Búsqueda imperativa en matriz
        for i in range(len(sillasg1)):
            for j in range(len(sillasg1[i])):
                if sillasg1[i][j] == sg:
                    sillasg1[i][j] = "x"  # Marcamos como ocupada
                    cant_g = cant_g + 1
                    total_g = total_g + 5000
                    encontrado = True
                    print(f"Silla {sg} agregada.")
                    break
            if encontrado == True:
                break
                
        if encontrado == False:
            print("Silla no disponible o no existe.")
            
        quiere_general = input("¿Desea otra silla GENERAL? (s/n): ")

    # --- CICLO PARA SILLAS VIP ---
    quiere_vip = input("\n¿Desea comprar sillas VIP? (s/n): ")
    while quiere_vip == "s":
        sv = int(input("Digite el numero de silla VIP que desea: "))
        encontrado = False
        
        # Búsqueda imperativa en lista
        for i in range(len(sillasvip)):
            if sillasvip[i] == sv:
                sillasvip[i] = "x"
                cant_v = cant_v + 1
                total_v = total_v + 10000
                encontrado = True
                print(f"Silla VIP {sv} agregada.")
                break
                
        if encontrado == False:
            print("Silla VIP no disponible o no existe.")
            
        quiere_vip = input("¿Desea otra silla VIP? (s/n): ")

    # Si no compró nada, salimos
    if cant_g == 0 and cant_v == 0:
        print("No se realizó ninguna compra.")
        return

    # --- DATOS DEL CLIENTE Y FACTURA ---
    nombre = input("\nDigite el nombre del cliente: ")
    numero_factura = len(facturas) + 1
    total_pagar = total_g + total_v
    
    print(f"\n--- Factura No {numero_factura} ---")
    print(f"Nombre: {nombre}")
    print(f"Sillas general: {cant_g}")
    print(f"Sillas VIP: {cant_v}")
    print(f"Total General: ${total_g}")
    print(f"Total VIP: ${total_v}")
    print(f"Total a pagar: ${total_pagar}")
    print("----------------------")
    
    # Guardamos los datos en la matriz de facturas
    facturas.append([numero_factura, nombre, cant_g, cant_v, total_g, total_v, total_pagar])


def menu_principal():
    # Matrices y listas inicializadas una sola vez
    sillasg1 = [
        [0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9]
    ]
    sillasvip = [10, 11, 12, 13, 14, 15]
    facturas = [] 
    
    ejecutando = True
    while ejecutando == True:
        print("\n\n----------- MENU -----------")
        print("1. Valor sillas")
        print("2. Comprar sillas")
        print("3. Buscar Factura")
        print("4. Cuadre de caja")
        print("5. Salir")

        eleccion = int(input("Ingresa una de las opciones: "))
        while eleccion < 1 or eleccion > 5:
            print("ERROR. Opcion no disponible.")
            eleccion = int(input("Ingresa una de las opciones: "))

        if eleccion == 1:
            valor_sillas(sillasg1, sillasvip)
            
        elif eleccion == 2:
            comprar_sillas(sillasg1, sillasvip, facturas)
            
        elif eleccion == 3:
            print("\n------- 3. BUSCAR FACTURA -------")
            buscar_nombre = input("Ingresa el nombre del cliente: ")
            encontrada = False
            
            for f in facturas:
                if f[1] == buscar_nombre:
                    print(f"\nFactura No {f[0]} encontrada:")
                    print(f"Cliente: {f[1]}")
                    print(f"Total pagado: ${f[6]}")
                    encontrada = True
                    break
            if encontrada == False:
                print("No hay facturas con ese nombre.")
                
        elif eleccion == 4:
            print("\n------- 4. CUADRE DE CAJA -------")
            total_caja = 0
            for f in facturas:
                total_caja = total_caja + f[6]
            print(f"El total recaudado en caja es: ${total_caja}")
            
        elif eleccion == 5:
            print("Saliendo del programa...")
            ejecutando = False

# Arrancar el programa
menu_principal()