n=int(input("Ingresa n:  "))
num=0
den=0
simb=""

for i in range(1,n+1):
    den=i*2
    num=den-1
    f=1
    for k in range(1,den+1):
        f=f*k
    print(simb,num,"/",f,end=",  ")
    if i%2==0:
        simb="+"
    else:
        simb="-"