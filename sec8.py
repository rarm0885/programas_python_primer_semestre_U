n=int(input("Ingresa n:  "))
simbol="-"
num=1
den=1
cont=0
for i in range (1,n+1):
    num=(i*2)-1
    den=i*5
    cont=cont+1
    if cont<3:
        simbol="-"
    if cont>2:
        simbol="+"
    if cont==4:
        cont=0
    print(simbol,num,"/",den,end=",  ")
    
