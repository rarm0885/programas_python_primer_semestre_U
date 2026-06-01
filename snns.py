n1=int(input('Ingresa n1: '))
n2=int(input('Ingresa n2: '))


if (n1+n2)<0:
    p=(n1+n2)/2
    print(p)
else:
    if (n1+n2)%2==0:
        print("Es par")
    else:
        print("Es impar")