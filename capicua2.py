print("################################################")
print("##CALCULADOR DE CAPICUA (numeros de 4 digitos)##")
print("################################################\n")

def valores():
    num4=int(input("Ingresa un numero de 4 digitos: "))
    while num4<1000 or num4>9999:
        num4=int(input("ERROR\nVuelve a ingresarlo:  "))
    uno=num4//1000
    dos=(num4%1000)//100
    tres=(num4%100)//10
    cuatro=num4%10
    return uno, dos, tres, cuatro

def es_capicua():
    v1,v2,v3,v4=valores()
    no_es_es_capicua= False
    
    while no_es_es_capicua==False:
        if v1==v4 and v2==v3:
            print("Tu numero es capicua...")
            no_es_es_capicua=True
        else:
            print("Tu numero no es capicua...")
            v1,v2,v3,v4=valores()
            if v1==v4 and v2==v3:
                print("Tu numero es capicua...")
                no_es_es_capicua=True
            


es_capicua()


