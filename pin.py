pin_secreto=1234
cont=3
while cont>0:
    vnumero=False
    while vnumero==False:
        numero=int(input("Ingresa un numero de cuatro digitos:\n"))
        if numero<1000 or numero>9999:
            print("Ingresa el numero de 4 digitos correctamente...\n")
        else:
            vnumero=True
    if numero==pin_secreto:
        print("Acceso concedico")
        break
    else:
        cont=cont-1
        print(f"Acceso denegado... te quedan {cont} intentos\n")
