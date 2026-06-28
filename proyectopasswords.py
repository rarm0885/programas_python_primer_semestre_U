password = str(input("Ingresa tu contraseña deseada:  "))
v=False
def validacion(password):
    tienenum=False

    for caracter in password:
        if caracter.isdigit():
            tienenum=True
            break

    return tienenum

while v==False:
    tienenum=validacion(password)
    if tienenum==False:
        print("Tu contraseña debe de contener al menos un numero...")
        password = str(input("Intentalo de nuevo:  "))
        tienenum=validacion(password)
    elif len(password)<=8:
        print("Tú contraseña debe de tener más de 8 caracteres...")
        password = str(input("Intentalo de nuevo:  "))
        tienenum=validacion(password)
    else:
        break
        
print("Tu contraseña es segura mi compa...") 
            

