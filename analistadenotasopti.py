notas_l=[]
num_notas=int(input("Ingresa tu numero de notas:\n"))
print("Ingresa tus notas...")
for i in range(num_notas):
        vnotas=False
        while vnotas==False:
            notas_i=float(input(""))
            if notas_i>5 or notas_i<0:
                print("Ingresa tu nota correctamente: ")
            else:
                notas_l.append (notas_i)
                vnotas=True
total_notas=0
for nota in notas_l:
     total_notas=total_notas+nota
prom=total_notas/num_notas
print(f"Tu promedio de notas fue de:\n {prom}")
