codigo=int(input("Ingresa tu codigo de 8 cifras YYYYSSNN:  "))
ano= codigo//10000
semestre= (codigo%10000)//100
estudiante= codigo%100
if codigo>99999999 or codigo<10000000:
    print("Ingresa el codigo correctamente...")
elif semestre>2 or semestre<1:
    print("Ingresa semestre correctamente...")
else:
    print(f"Ingresaste a la U en el ano lectivo {ano}, primer semestre, siendo el estudiante numero {estudiante} ")
