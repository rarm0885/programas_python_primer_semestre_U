
def verificacion_edad():
    
    edad=int(input("Ingresa tu edad: "))
    if edad<0:
        print("Ingresa bien tu edad...")
    return edad

def verificacion_pase_vip(): 
    
    pase_vip=False
    tiene_pase_vip=input("Tienes pase VIP?? (si/no).\n ")
    if tiene_pase_vip=="Si" or tiene_pase_vip=="SI":
        pase_vip=True
    return pase_vip


def verificacion_final(edad,pase_vip):
    
    if edad>=18:
        print("Puedes pasar...")
    else:
        if edad<18 and pase_vip==True:
            print("Puedes pasar chiqui...")
        else:
            print("No puedes pasar chiqui...")


edad_usuario=verificacion_edad()
usuario_vip=verificacion_pase_vip()
verificacion_final(edad_usuario, usuario_vip)
