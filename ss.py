#Se va a ingresar una fecha por día mes año y hora por ejemplo
#30 10 2025 10 22
#Es decir, el código dirá la diferencia de días, meses, años, hora, y minutos
#Reconocerá si es un año bisiesto y tendrá las limitaciones, tomando la hora como desde 00 hasta 23:59

f1=int(input("PRIMERA FECHA: Ingresa dia/mes/ano/hora/minutos: "))
dia1=f1//10000000000
mes1=(f1%10000000000)//100000000
ano1=(f1%100000000)//10000
hora1=(f1%10000)//100
minuto1=(f1%100)

f2=int(input("SEGUNDA FECHA: Ingresa dia/mes/ano/hora/minutos: "))
dia2=f2//10000000000
mes2=(f2%10000000000)//100000000
ano2=(f2%100000000)//10000
hora2=(f2%10000)//100
minuto2=(f2%100)

#Esto es para regular los meses1
if mes1>12 or mes1<1:
    print("Ingresa bien el mes de la primera fecha")

#Esto es para regular los dias1 del mes1
if mes1==1:
    if dia1>31 or dia1<1:
        print("Ingresa bien el dia")

if mes1==2:
    if dia1>28 or dia1<1:
        print("Ingresa bien el dia")

if mes1==3:
    if dia1>31 or dia1<1:
        print("Ingresa bien el dia")

if mes1==4:
    if dia1>30 or dia1<1:
        print("Ingresa bien el dia")

if mes1==5:
    if dia1>31 or dia1<1:
        print("Ingresa bien el dia")

if mes1==6:
    if dia1>30 or dia1<1:
        print("Ingresa bien el dia")

if mes1==7:
    if dia1>31 or dia1<1:
        print("Ingresa bien el dia")

if mes1==8:
    if dia1>31 or dia1<1:
        print("Ingresa bien el dia")

if mes1==9:
    if dia1>30 or dia1<1:
        print("Ingresa bien el dia")

if mes1==10:
    if dia1>31 or dia1<1:
        print("Ingresa bien el dia")

if mes1==11:
    if dia1>30 or dia1<1:
        print("Ingresa bien el dia")

if mes1==12:
    if dia1>31 or dia1<1:
        print("Ingresa bien el dia")

#Esto es para saber si es bisiesto 1
if ano1%4==0:
    print("El",ano1,"es bisiesto...")
else:
    print("El",ano1,"no es bisiesto...")

#esto es para limitar las horas1 y los segundos1
if hora1>23 or hora1<1:
    print("Ingresa bien la hora")
if minuto1>59 or minuto1<1:
    print("Ingresa bien los minutos")



#Esto es para regular los meses2
if mes2>12 or mes2<1:
    print("Ingresa bien el mes de la segunda fecha")

#Esto es para regular los dias 2
if mes2==1:
    if dia2>31 or dia2<1:
        print("Ingresa bien el dia2")

if mes2==2:
    if dia2>28 or dia2<1:
        print("Ingresa bien el dia2")

if mes2==3:
    if dia2>31 or dia2<1:
        print("Ingresa bien el dia2")

if mes2==4:
    if dia2>30 or dia2<1:
        print("Ingresa bien el dia2")

if mes2==5:
    if dia2>31 or dia2<1:
        print("Ingresa bien el dia2")

if mes2==6:
    if dia2>30 or dia2<1:
        print("Ingresa bien el dia2")

if mes2==7:
    if dia2>31 or dia2<1:
        print("Ingresa bien el dia2")

if mes2==8:
    if dia2>31 or dia2<1:
        print("Ingresa bien el dia2")

if mes2==9:
    if dia2>30 or dia2<1:
        print("Ingresa bien el dia2")

if mes2==10:
    if dia2>31 or dia2<1:
        print("Ingresa bien el dia2")

if mes2==11:
    if dia2>30 or dia2<1:
        print("Ingresa bien el dia2")

if mes2==12:
    if dia2>31 or dia2<1:
        print("Ingresa bien el dia2")

#Esto es para saber si es bisiesto 
if ano2%4==0:
    print("El",ano2,"es bisiesto...")
else:
    print("El",ano2,"no es bisiesto...")

#esto es para limitar las horas2 y los segundos2
if hora2>23 or hora2<1:
    print("Ingresa bien la hora2")
if minuto2>59 or minuto2<1:
    print("Ingresa bien los minutos2")



# Restamos minutos
difminuto = minuto2 - minuto1
if difminuto < 0:
    difminuto = difminuto + 60
    hora2 = hora2 - 1  # Pedimos prestado a la hora

# Restamos horas
difhora = hora2 - hora1
if difhora < 0:
    difhora = difhora + 24
    dia2 = dia2 - 1    # Pedimos prestado al día


# Restamos días
difdia = dia2 - dia1
if difdia < 0:
    # Debemos saber cuántos días tenía el mes anterior a mes2
    mes_anterior = mes2 - 1
    ano_aux = ano2
    
    if mes_anterior == 0: # Si era enero, el anterior es diciembre del año pasado
        mes_anterior = 12
        ano_aux = ano2 - 1
        
    # Determinamos cuántos días sumarle a la diferencia negativa
    dias_del_mes = 0
    if mes_anterior == 2:
        # Verificamos si ano_aux es bisiesto
        if (ano_aux % 4 == 0 and ano_aux % 100 != 0) or (ano_aux % 400 == 0):
            dias_del_mes = 29
        else:
            dias_del_mes = 28
    elif mes_anterior == 4 or mes_anterior == 6 or mes_anterior == 9 or mes_anterior == 11:
        dias_del_mes = 30
    else:
        dias_del_mes = 31
        
    difdia = difdia + dias_del_mes
    mes2 = mes2 - 1 # Pedimos prestado al mes


# Restamos meses
difmes = mes2 - mes1
if difmes < 0:
    difmes = difmes + 12
    ano2 = ano2 - 1 # Pedimos prestado al año

# Restamos años
difano = ano2 - ano1
    
print(f"La diferencia es: {difano} años, {difmes} meses, {difdia} días, {difhora} horas y {difminuto} minutos.")





#301020251022