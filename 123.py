n=int(input("Ingresa n: "))
if n>999 or n<100:
    print("Ingresa bien n")
n1=n//100
n2=(n%100)//10
n3=n%10
num=["cero","uno","dos","tres","cuatro","cinco",'seis','siete','ocho','nueve']

print(num[n1],num[n2],num[n3])