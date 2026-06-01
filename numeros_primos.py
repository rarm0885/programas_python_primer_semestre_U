n=int(input("Ingresa el numero:  "))
flag=True
if n<=1:
    flag=False
else:
    for i in range(2,n):
        if n%i==0:
            flag=False
            break
if flag==True:
    print(f"{n} es primo...")
else:
    print(f"{n} no es primo...")
