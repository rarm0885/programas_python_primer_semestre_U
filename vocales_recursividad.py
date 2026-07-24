def contar_vocales(palabra):
    if len(palabra) == 0:
        return 0
    es_vocal = 1 if palabra[0] in "AEIOUaeiou" else 0

    return es_vocal + contar_vocales(palabra[1:])

print(contar_vocales("aura"))