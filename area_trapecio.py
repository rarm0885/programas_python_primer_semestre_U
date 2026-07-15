a, b, m = map(int,input("Ingresa Altura(a), Base menor(b) y la Base mediana(m):  ").split())

c = (2*m)-b
area_trapecio = ((c+b)*a)/2

print(area_trapecio)