a=1
b=0
c=1
A=2
B=2
C=2
simbolo=""
cont=1
for i in range (1,16):
        cont=cont+1
    if i<3:
        simbolo="-"
    else:
        simbolo="+"
    if cont==6:
        cont=0
    
    print(simbolo,c,end="/",)
    print(C)
    a=b
    b=c
    c=a+b
    A=B
    B=C
    C=A+B
    cont=cont+1
    if i<3:
        simbolo="-"
    else:
        simbolo="+"
    if cont==6:
        cont=0



