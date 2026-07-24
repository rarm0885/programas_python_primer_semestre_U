def detector_palindromo(palabra):
    if len(palabra) <= 1:
        return True

    if palabra[0] != palabra[-1]:
        return False
    else:
        centro_de_palabra = palabra[1:-1]

        return detector_palindromo(centro_de_palabra)
    

print(detector_palindromo("recursivir"))