def edad():
    edad=int(input("Igresa tu edad:  "))
    while edad<1 or edad>117:
        edad=int(input("Pusiste tu edad incorrectamente...\nIngresa tu edad de nuevo: "))
    return edad

def vip():
    v_vip=False
    eres_vip=False
    vip=input("Eres usuario VIP? (si o no) ")
    while v_vip==False:
        if vip=="SI" or vip=="Si" or vip=="si":
            eres_vip=True
            v_vip=True
        else:
            if vip=="NO" or vip=="No" or vip=="no":
                v_vip=True
            else:
                vip=input("Ingresa el apartado VIP correctamente (si o no)...\nEres usuario VIP? ")
    return eres_vip

def inicio(ed,vipp):
    if ed>=18:
        print("Puedes pasar, no necesitas VIP...")
    else:
        if ed<18 and vipp==True:
            print("Puedes pasar usuario VIP...")
        else:
            print("No puedes pasar, necesitas VIP...")

ed=edad()
vipp=vip()
inicio(ed,vipp)
        

