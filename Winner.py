# Leemos la cantidad de rondas
n_rounds = int(input())

# Preparamos nuestras herramientas
top = {}                # Libreta para el puntaje final
winner = []             # Club VIP (candidatos al premio)
record = []             # Nuestra "máquina del tiempo" (historial del partido)
temporary_points = {}   # Libreta en blanco para el desempate

# --- VIAJE 1: EL PARTIDO ---
for i in range (0, n_rounds):

    # input().split() recorta el texto por el espacio (ej. "Juan 15" -> ["Juan", "15"]).
    # Python es capaz de repartir ("desempaquetar") esos pedazos en 'name' y 'score' en una sola línea.
    name, score = input().split()
    score = int(score)
    
    # .get(name, 0) es el salvavidas: "Dame los puntos de 'name', pero si no existe, dame un 0".
    # Esto evita que el programa explote (KeyError) en el primer turno de un jugador.
    top[name] = top.get(name, 0) + score
    
    # .append() guarda cosas al final de la lista. 
    # Los corchetes [] extra empaquetan el nombre y los puntos juntos como un solo elemento.
    record.append([name, score])


# --- EL PITAZO FINAL ---
# .values() ignora los nombres y extrae una lista solo con los puntajes. 
# max() mira esa lista y te devuelve el número más grande.
highest = max(top.values())

# .items() desempaqueta el diccionario. En cada vuelta te entrega la pareja exacta: llave (name) y valor (score).
for name, score in top.items():
    if score == highest:
        winner.append(name)


# --- VIAJE 2: EL DESEMPATE ---
# Recorremos la lista 'record'. Como cada elemento era una listita [name, score], 
# Python la vuelve a desempaquetar automáticamente.
for name, score in record:
    
    # Llevamos la cuenta desde cero en nuestra libreta temporal
    temporary_points[name] = temporary_points.get(name, 0) + score
    
    # LA CONDICIÓN DE VICTORIA:
    # 1. 'in' es un operador de pertenencia. Verifica si 'name' existe dentro de la lista 'winner'.
    # 2. 'and' obliga a que ambas condiciones se cumplan al mismo tiempo.
    if name in winner and temporary_points[name] >= highest:
        print(name)
        
        # 'break' es el freno de emergencia. Al encontrar al ganador, destruye el ciclo 'for' 
        # para que no siga buscando ni imprimiendo más nombres.
        break




            