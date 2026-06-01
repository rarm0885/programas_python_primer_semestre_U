n=int(input("Ingresa tu numero de 3 digitos:  "))
if n>999 or n<100:
    print("Ingresa bien tu numero")
else:
    centena=n//100
    if centena%2==0:
        print(f"El numero que representa tu centena es par ({centena})")
    else:
        print(f"El numero que representa tu centena es impar ({centena})")
