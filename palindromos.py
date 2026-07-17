def longitud (texto):
    longi = 0
    for letra in texto:
        longi += 1
    return longi

def palindromo (texto):
    longi = longitud(texto)
    for i in range (1,longi+1):
        for letra in texto:
            if letra == texto[-i]:
                return True
            else:
                return False

valor = palindromo("oso")
print(valor)
