def sumar_lista(lista):
    if len(lista) == 0:
        return 0 
    return lista [0] + sumar_lista(lista[1:])

lista = [3,2,1]
print(sumar_lista(lista))
