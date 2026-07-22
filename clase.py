#Se importan las librerias time (Sirve para manejar tiempo en el codiguin) y sys ()
import time 
import sys

#animaciones con sys

def animacion_salida():
    frames = [
        "Saliendo.",
        "Saliendo..",
        "Saliendo...",
        "Gracias por jugar"
    ]

    for frame in frames:
        sys.stdout.write('\r' + frame)
        sys.stdout.flush()
        time.sleep(0.9)

def animacion_meta():
    texto = "FELICITACIONES, COMPLETARON EL JUEGO CON EXITO"
    
    print("\n")

    for i in range (len(texto)+1):

        frame = "🏆" + texto[i:]
        sys.stdout.write('\r' + frame)
        sys.stdout.flush()
        time.sleep(0.1)


def animacion_par():
    #frames para la animacion
    frames = [
        f"{'👋 o         👋':^25}",
        f"{'👋   o       👋':^25}",
        f"{'👋     o     👋':^25}",
        f"{'👋       o   👋':^25}",
        f"{'👋         o 👋':^25}"
    ]
    
    for frame in frames:
        # \r sobrescribe la línea actual en la consola
        sys.stdout.write('\r' + frame)
        sys.stdout.flush() # Fuerza a la consola a dibujar inmediatamente
        time.sleep(0.1)    # Pausa de 0.1 segundos por fotograma
        
    print() # Un salto de línea al final para que el siguiente texto no se pegue

def animacion_impar():
    frames = [
        f"{'👋         o👋':^25}",
        f"{'👋       o  👋':^25}",
        f"{'👋     o    👋':^25}",
        f"{'👋   o      👋':^25}",
        f"{'👋 o        👋':^25}"
    ]

    for frame in frames:
        sys.stdout.write('\r' + frame)
        sys.stdout.flush()
        time.sleep(0.1)
    print()



#Aca de definen los ingresos y se hace un Try, Except para controlar errores
def inputs():
    while True:
        try:
            n_jugadores = int(input("Ingresa el numero de Jugadores:  "))
            break
        except ValueError:
            print("Solo puedes ingresar un numero entero, recuerdalo...")
            print()

    while True:
        try:
            puntaje = int(input("Ingresa el Puntaje Maximo para ganar:  "))
            break
        except ValueError:
            print("Solo puedes ingresar un numero entero, recuerdalo...")

    return n_jugadores,puntaje


#Aca se crea la logica del juego y se hace  que funcione llamando las otras definiciones
def juego():
    n_jugadores,puntaje = inputs()
    posicion_jugador = 0
    valor = 0
    acu = 1

    while valor < puntaje:
        
        if posicion_jugador % 2 == 0:
            valor = valor + 2
            
            animacion_par()
            
            print(f"{'='*30:<30}")
            print (f"Jugador {acu:<3}: Puntaje {valor:>3}")
            print(f"{'='*30:<30}")


        
        elif posicion_jugador%2==1:
            valor = valor-1
            
            animacion_impar()
            
            print(f"{'='*30:<30}")
            print (f"Jugador {acu:<3}: Puntaje {valor:>3}")
            print(f"{'='*30:<30}")

        acu = acu + 1
        
        posicion_jugador = posicion_jugador + 1
        
        if acu == n_jugadores:
            acu = 0 

        time.sleep(0.5)

    print()
    animacion_meta()


def menu():
    print()
    print(f"{'*'*60}")
    print(f"{'BIENVENIDO AL MEJOR JUEGO DEL MUNDO':^60}")
    print(f"{'EL JUEGO DE LA PELOTA (SUMAS Y RESTAS)':^60}")
    print(f"{'*'*60}\n")
    print("1. Jugar.\n")
    print("2. Salir.\n")

    while True:
        try:
            eleccion_menu = int(input("Ingresa alguna de las dos opciones del menú:\n"))
            break
        except ValueError:
            print("Solo puedes ingresar (1 o 2)...")

    if eleccion_menu == 1:
        juego()
        menu()
    elif eleccion_menu == 2:
        print()
        animacion_salida()


menu()
    

