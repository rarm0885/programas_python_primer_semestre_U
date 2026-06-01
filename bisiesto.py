yyyymmdd=int(input("Ingresa YYYYMMDD: "))
yyyy=yyyymmdd//10000
if yyyy%4==0:
    print(yyyy,"es un ano bisiesto...")
else:
    print(yyyy,'no es un ano bisiesto...')
