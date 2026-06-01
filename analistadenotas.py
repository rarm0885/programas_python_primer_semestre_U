notas=[1.0,5.0,4.0,3.5,5]
num_notas=len(notas)
suma_total=0
for i in range (num_notas):
    suma_total=suma_total+notas[i]
prom=(suma_total/num_notas)
print(f"El promedio de tus notas es:\n {prom}")
