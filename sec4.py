n=int(input("Ingresa n:  "))
simbol=""
a=2
b=2
c=2
for i in range(1,n+1):
    if i%2==0:
        simbol="+"
    else:
        simbol="-"
    print(simbol,c,end=", ")
    a=b
    b=c
    c=a+b
    