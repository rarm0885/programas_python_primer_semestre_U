n=int(input("Ingresa n:  "))
num=0
den=0
simb=""

for i in range(1,n+1):
    den=i*2
    num=(den-1)**den
    print(simb,num,"/",den,end=",  ")
    if i%2==0:
        simb="+"
    else:
        simb="-"