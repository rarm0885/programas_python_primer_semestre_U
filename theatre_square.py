n,m,a = map(int,input().split())
if (n<1 or m<1 or a<1) or (n>10**9 or m>10**9 or a>10**9):
    print("Type the variables correctly")
else:
    #se calcula ancho y alto, y luego, se multiplican
    print((((n+a)-1)//a)*(((m+a)-1)//a))