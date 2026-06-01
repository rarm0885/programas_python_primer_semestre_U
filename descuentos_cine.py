#Hay descuento en el cine si y solo si ed<25 y v_carnet==True. Sino se paga el precio completo 

def edad():
    v_ed=False
    while v_ed==False:
        ed=int(input("Ingresa tu edad broski: \n"))
        if ed<1 or ed>117:
            print("Ingresa correctamente el formulario de edad...")
        else:
            v_ed=True
            return ed

def carnet():
    v_carnet=False
    tiene_carnet=False
    while v_carnet==False:
        carnet_estudiantil=input("Tienes Carnet estudiantil??.\n (si/no):  ")
        if carnet_estudiantil=="SI" or carnet_estudiantil=="si" or carnet_estudiantil=="Si" or carnet_estudiantil=="NO" or carnet_estudiantil=="no" or carnet_estudiantil=="No":
            if carnet_estudiantil=="SI" or carnet_estudiantil=="si" or carnet_estudiantil=="Si":
                tiene_carnet=True
            v_carnet=True
        else:
            print("Ingresa correctamente el formulario Carnet Estudiantil...")
    return tiene_carnet

def final(edadv,carnetv):
    if edadv<25 and carnetv==True:
        print("Aplicas para el descuento...")
    else:
        print("No aplicas para el descuento...")

edadv=edad()
carnetv=carnet()

final(edadv,carnetv)

