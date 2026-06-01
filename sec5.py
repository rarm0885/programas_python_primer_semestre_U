n=int(input("Ingresa n:  "))
simbol=""
num=0
den=0
for i in range(1,n+1):
    den=i*2
    num=den-1
    print(simbol,num,"/",den,end=",  ")
    if i%2==0:
        simbol="+"
    else:
        simbol="-"
        
    
    
