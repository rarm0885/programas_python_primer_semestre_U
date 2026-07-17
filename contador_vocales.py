#Recorre el texto y cuenta las vocales

def contar_vocales(texto):
    cont = 0
    vocales = "aeiouAEIOU"

    for letra in texto:
        for vocal in vocales:
            if letra == vocal:
                cont = cont + 1
    
    return cont

cont = contar_vocales("buuenas")
print(cont)