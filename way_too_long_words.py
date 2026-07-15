#la funcion sep="" sirve para que no hayan espacios dentro de un print...

#aunque python lee los str como arreglos (desde 0 hasta ...), la funcion len() los lee como un humano, (desde 0 hasta ...)
n = int(input())
for i in range (0,n):
    w = (input("")).lower()

    if n<1 or n>100:
        print("Typer w correctly")
        break
    
    else:
        if len(w)<11:
            print(w)
        else:
            length = len(w) - 2
            f = w[0]
            l = w[(len(w)-1)]
            print(f,length,l,sep="")

