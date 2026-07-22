def suma_lista(numero): 
    if len(numero) == 0:
        return 0
    else:
        return numero[0] + suma_lista(numero[1:])

lista = [1,3,4,6,7]
re = suma_lista(lista)
print(re)