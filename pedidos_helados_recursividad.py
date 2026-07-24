print("--BIENVENIDO A HELADERIA CHUPALA--")
total = 0
historial_ventas = []
def menu ():
    print()
    print("1. Chocolate: 3$.")
    print("2. Vainilla: 2$.")
    print("3. Ver Historial de Ventas.")
    print("4. Salir")
    print()

    pedidos(total,historial_ventas)


def definicion_eleccion(total,historial_ventas):
    eleccion = input("Deseas otro Helado (si o no):\n").lower()
    if eleccion == "si" or eleccion =="no":
        if eleccion == "si":
            pedidos(total,historial_ventas)
        elif eleccion == "no":
            print(f"Tu total es: {total}$")
            historial_ventas.append(total)

            menu()
                        
        else:
            print("Opcion no valida...")
            definicion_eleccion(total,historial_ventas)
        
    return historial_ventas


def pedidos (total,historial_ventas):
    chocolate = 3
    vainilla = 2

    try:
        opcion = int(input("Ingresa la opcion que deseas:\n"))
    except ValueError:
        menu()

    if opcion > 4 or opcion <1:
        print("ERROR: Esa opcion no existe...")
        menu()

    if opcion == 1:
        print(f"Son {chocolate}$.\n")
        total = total + chocolate

        historial_ventas = definicion_eleccion(total,historial_ventas) 
 
    elif opcion == 2:
        print(f"Son {vainilla}$.\n")
        total = total + vainilla

        historial_ventas = definicion_eleccion(total,historial_ventas) 

    elif opcion == 3:
        print("--HISTORIAL VENTAS--")
        imprimir_historial(historial_ventas)
        menu()



    return total


def imprimir_historial(historial_ventas,x=1):
    print()
    if historial_ventas == []:
        return None
    else:
        print(f"{x}. {historial_ventas[0]}")
        imprimir_historial(historial_ventas[1:],x+1)



menu()
        




