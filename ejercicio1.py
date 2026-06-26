def variables(): 
    print("--------CALCULADORA DEL TALLER 1--------")
    print("INGRESA LAS VARIABLES QUE DESEAS USAR \n")
    print("Nota: Estas variables se usaran para todos los puntos... \n")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    x = float(input("x = "))

    return a,b,c,x



def e1(a):
    if a==5:
        return ("ERROR")
    else:
        return ((100-200)/a-5)
    
def e2(a):
    return (15-(a**2/3))

def e3(a,b,c):
    return (a**2+b**2-(35*c))

def e4(x):
    return ((5*x**2)-(3*x)+5)

def e5(a,b):
    if a<0 or b<0:
        return ("ERROR")
    else:
        return ((a**0.5)+((b**3)**0.5))

def e6(a):
    return (a**10-5)

def menu():
    print("--------------------------_MENU_--------------------------\n\n")
    print("1. RESOLVER TODOS LOS PUNTOS DEL TALLER 1, PREGUNTA 1.\n")
    print("2. SALIR.\n")
    print("digita alguna de las opciones en pantalla:",end=(" "))
    
    eleccion = int(input(""))
    while True:
        if eleccion==1 or eleccion==2:
            break
        else:
            eleccion = int(input("Ingresa tu elección correctamente:  "))
    
    if eleccion == 1:
        
        a,b,c,x = variables()
        error1 = ""
        error2 = ""
        if a==5:
            error1 = "Nota: El punto a. te da ERROR debido a que el denominador\n en una division no puede ser 0 y (5-5=0)..."
        
        if a<0 or b<0:
            error2 = "Nota: El punto e. te da ERROR debido a que una raiz par\n no puede ser menor a 0... "
        
        print(f"""
*****************************************************************************************
*                                                                                          
*  
*    a.   100 - 200                                   b.     15 - A^2                                       
*       ---------  = {e1(a)}                                    ---  = {e2(a)}                           
*         A - 5                                                  3                                       
*                                                                                       
*                                                                                      
*                                                                                   
*  
*    c.   a^2 + b^2 - 35c  = {e3(a,b,c)}              d.    5X^2 - 3 X + 5  = {e4(x)}                      
*                                                                                       
*                                                                                       
*                                                                                      
*  
*    e.   √a + √b^3  = {e5(a,b)}                      f.    a^10 - 5  = {e6(a)}                                                       
*                                                                                       
*                                                                                       
*                                                                                     
*                                                                 
*                                                                                       
*                                                                                       
*                                                                                       
*                                                                                       
*                                                                                       
*                                                                                       
*  {error1}                                                                             
*                                                                                       
*  {error2}                                                                             
*
*                                                                                           
*****************************************************************************************
       """)
        
        
        menu()

    
    elif eleccion == 2:
        print("Saliendo")
        print("Saliendo.")
        print("Saliendo..")
        print("Saliendo...")
        print("Listo, hasta luego👋")   


menu()






