n = int(input("Ingresa un número positivo menor a 257: "))

# Filtramos para asegurarnos de que cumpla las reglas del enunciado
if n <= 0 or n >= 257:
    print("¡Ojo! El número debe ser positivo y menor a 257.")
else:
    binario = ""  # Aquí vamos a ir armando nuestro texto con los 1 y 0
    
    # El for da máximo 9 vueltas, que es lo máximo que ocupa el número 256
    for i in range(9):
        residuo = n % 2
        
        # SÚPER TRUCO: Sumar textos. Pegamos el nuevo dígito a la IZQUIERDA.
        binario = str(residuo) + binario
        
        # División entera. Usamos // para que no nos queden decimales
        n = n // 2
        
        # La salida de emergencia si terminamos antes de las 9 vueltas
        if n == 0:
            break
            
    print(f"El número en sistema binario es: {binario}")