n=int(input("Ingrese su numero de 4 cifras: "))
if n>9999 or n<1000 or n<0:
    print("Ingresa tu numero de 4 cifras correctamente...")
else: 
    if n%3==0 and n%6==0:
        print("Tu numero es multiplo de 3 y de 6...")
    elif n%3==0:
        print("Tu numero es multiplo de 3 pero NO de 6")
    elif n%6==0:
        print("Tu numero es multiplo de 6 mas NO de 3...")
    else:
        print("Tu numero no es multiplo ni de 3 ni de 6...")
