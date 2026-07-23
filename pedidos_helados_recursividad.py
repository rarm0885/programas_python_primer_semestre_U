print("BIENVENIDO A HELADERIA CHUPALA")
pedido = 0
def menu ():
    print()
    print("1. Chocolate: 3$")
    print("2. Vainilla: 2$")
    print("3. Salir")
    print()

    pedidos(pedido)


def pedidos (pedido):
    chocolate = 3
    vainilla = 2

    try:
        opcion = int(input("Ingresa la opcion que deseas:\n"))
    except ValueError:
        menu()

    if opcion > 3 or opcion <1:
        print("ERROR: Esa opcion no existe...")
        menu()

    if opcion == 1:
        print(f"Son {chocolate}$.\n")
        pedido = pedido + chocolate

        eleccion = definicion_eleccion()
        if eleccion == "si" or eleccion =="no":
            if eleccion == "si":
                pedidos(pedido)
            elif eleccion == "no":
                print(f"Tu total es: {pedido}$")
                
        else:
            print("Opcion no valida...")
            eleccion = definicion_eleccion()

    elif opcion == 2:
        print(f"Son {vainilla}$.\n")
        pedido = pedido + vainilla

        eleccion = definicion_eleccion()
        if eleccion == "si" or eleccion =="no":
            if eleccion == "si":
                pedidos(pedido)
            elif eleccion == "no":
                print(f"Tu total es: {pedido}$")
                
        else:
            print("Opcion no valida...")
            eleccion = definicion_eleccion()



    return pedido

def definicion_eleccion():
    eleccion = input("Deseas otro Helado (si o no):\n").lower()
    return eleccion 

menu()
        




