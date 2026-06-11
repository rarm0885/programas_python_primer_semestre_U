def valor_sillas(sillasg1,sillasvip):
    #el menu de los valores de las sillas, validaciones, y las sillas que hay
    print("\n\n-------VALOR SILLAS-------")
    print("\n1. Silla General")
    print("\n2. Silla VIP")
    print("\n3. Mostrar Valores")
    print("\n---------------------------")
    menu_valor_sillas=int(input("\nIngresa alguna de las opciones:\n"))
    verificacion_op=False
    while verificacion_op==False:
        if menu_valor_sillas==1 or menu_valor_sillas==2 or menu_valor_sillas==3:
            verificacion_op=True
            break
        else:
            print(f"ERROR. Opcion {menu_valor_sillas} No existe...")
            menu_valor_sillas=int(input("Ingresa alguna de las opciones nuevamente:\n"))

    while menu_valor_sillas<4 and menu_valor_sillas>0:
        if menu_valor_sillas==1:
            print("El valor de las sillas Generales es de $5000")
            menu()
            break
        if menu_valor_sillas==2:
            print("El valor de las sillas VIP es de $10000")
            menu()
            break
        if menu_valor_sillas==3:
            for fila in sillasg1:
                print(fila,"\n")
            print(sillasvip,end=" ")
            print("\n")
            menu()
            break


def comprar_sillas(sillasg1,sillasvip,facturas):
    comprador=[]
    print("\n\n-------COMPRAR SILLAS-------")
    print("\n1. Silla General")
    print("\n2. Silla VIP")
    print("\n3. Ambas")
    print("\n4. Salir al menú")
    v=False
    comprar_silla=int(input("Que tipo de silla deseas comprar?\n"))
    while v==False:
        if comprar_silla==1 or comprar_silla==2 or comprar_silla==3 or comprar_silla==4:
            v=True
            break
        else:
            print(f"ERROR. No existe la opcion {comprar_silla}\nIntentalo de Nuevo...")
            comprar_silla(input("Que tipo de silla deseas comprar?\n"))

    nombre=str(input("Ingresa nombre de comprador:  "))
    comprador.append(nombre)

    numero_sillasg=0
    numero_sillasv=0
    
    if comprar_silla==1:
        sg=int(input("Que numero de silla GENERAL deseas comprar?\n"))
        
        for i in range (len(sillasg1)):
            for j in range (len(sillasg1[i])):
                if sillasg1[i][j]==sg:
                    sillasg1[i][j]="x"
                    numero_sillasg=numero_sillasg+1
            else:
                print("Esta silla no esta disponible...")
                    
                    
        if comprar_silla==2:
            sv=int(input("Que numero de silla VIP deseas comprar?\n"))
            for i in sillasvip:
                if sv!="x":
                    sillasvip[i]="x"

        if comprar_silla==4:
            menu()

        return sillasg1,sillasvip


def menu():
    
    sillasg1=[
        [0,1,2,3,4],
        [5,6,7,8,9]
    ]
    sillasvip=[10,11,12,13,14,15]
    facturas=[]
    
    print("\n\n-----------MENU-----------")
    print("1.Valor sillas")
    print("2.Comprar sillas")
    print("3.Buscar Factura")
    print("4.Cuadre de caja")
    print("5.Salir")

    verificacion=False
    while verificacion==False:
        eleccion=int(input("Ingresa una de las opciones:  "))
        if eleccion==1 or eleccion==2 or eleccion==3 or eleccion==4 or eleccion==5:
            verificacion=True
            break
        else:
            print(f"ERROR. La opcion {eleccion} no esta disponible")
            eleccion=int(input("Ingresa una de las opciones:  "))
            

    if eleccion==1:
        valor_sillas(sillasg1,sillasvip)
    if eleccion==2:
        comprar_sillas(sillasg1,sillasvip,facturas)
    if eleccion==3:
        print("no disponible")
        menu()
    if eleccion==4:
        print("no disponible")
        menu()
menu()
        
    
        
                        
            
            
        










            
    


    
            
    
