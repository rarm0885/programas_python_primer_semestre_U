n_jugadores = 12
posicion_jugador = 0
n = 0
puntaje = 12

while n<puntaje:
    
    if posicion_jugador%2==0:
        n = n + 2
        print(f"Jugador {posicion_jugador:<3}: Puntaje {n:>3}")
    
    elif posicion_jugador%2==1:
        n = n-1
        print(f"Jugador {posicion_jugador:<3}: Puntaje {n:>3}")
    
    posicion_jugador = posicion_jugador + 1
    
    if posicion_jugador == n_jugadores:
        posicion_jugador = 0 
