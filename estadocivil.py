#Elaborar un algoritmo que lea el nombre, la edad, el sexo y el estado civil de cualquier
#persona e imprima el nombre de la persona; solo si, corresponde a un hombre casado,
#mayor de 40 años o una mujer soltera menor de 50 años, y un mensaje que así lo indique. 

nom=input("Ingresa tu nombre: ")
ed=int(input("Ingresa tu edad: "))
sex=int(input("Ingresa tu sexo (Masculino=1 y Femenino=2) : "))
ec=int(input("Soltero=1 o Casado=2: "))
s=[1,2]
if sex not in s :
    print("Ingresa bien tu sexo cacorro...")
elif ec not in s :
    print("Ingresa bien tu putisimo Estado Civil bimbimbambam...")

else:
    if (sex==1 and ec==2 and ed>40) or (sex==2 and ec==1 and ed<50):
        print(nom,"Si aplicas...")
    else:
        print("Lo sentimos",nom,"no aplicas...n")
      
