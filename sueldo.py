tipo_empleado=int(input("Ingresa que tipo de empleado eres (del 1 al 4):  "))
sueldo=int(input("Ingresa tu sueldo Actual:  "))
if tipo_empleado<1 or tipo_empleado>4:
    print("Ingresa bien tu tipo de empleado...")
elif sueldo<1:
    print("Tu sueldo no puede ser negativo...")
else: 
    if tipo_empleado==1 or tipo_empleado==2:
        aumento= sueldo*0.05
        st= aumento+sueldo
        print(f"FELICIDADES, tu aumento fue de: {aumento} y tu sueldo total actual es: {st}")
    if tipo_empleado==3 or tipo_empleado==4:
        aumento= sueldo*0.12
        st= aumento+sueldo
        print(f"FELICIDADES, tu aumento fue de: {aumento} y tu sueldo total actual es: {st}")