mapa_tesoro=[
    ["","X",""],
    ["","","X"],
    ["X","",""]
]
mapa_tesoro[1][1]="T" 
mapa_tesoro[2][2]="O"

for fila in mapa_tesoro:
    for casilla in fila:
        print(casilla,end=" ")
    print()