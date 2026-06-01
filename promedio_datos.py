n=int(input("Ingresa la cantidad de datos que deseas ingresar al algoritmo:  "))
cont=0
acu=0
print("Ingresa los numeros...")
for i in range(n):
    nums=float(input(""))
    acu=acu+nums
    cont=cont+1
promedio=acu/cont
print(f"Este es el promedio de tus datos: {promedio}")



