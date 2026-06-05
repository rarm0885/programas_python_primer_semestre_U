

def crear_empleado():
    print("##########-CREAR EMPLEADO-##########")
    numeros=["0","1","2","3","4","5","6","7","8","9"]
    datos_este_empleado=[]

    verificacion_nombre=False
    verificacion_apellido=False
    verificacion_id=False 
    verificacion_edad=False
    verificacion_tipo=False
    
    nombre=str(input("Ingresa tu nombre:\n"))
    while verificacion_nombre==False:
        tiene_error=False
        for caracteres in nombre:
            for num in numeros:
                if caracteres==num:
                    tiene_error=True
        if tiene_error==True:
            nombre=str(input("Ingresa tu nombre correctamente:\n"))
        else:
            verificacion_nombre=True
            break
    datos_este_empleado.append(nombre)
    
    apellido=str(input("Ingresa tus apellidos:\n"))
    while verificacion_apellido==False:
        tiene_error=False
        for caracteres in apellido:
            for num in numeros:
                if caracteres==num:
                    tiene_error=True
        if tiene_error==True:
            apellido=str(input("Ingresa tus apellidos correctamente:\n"))
        else:
            verificacion_apellido==True
            break
    datos_este_empleado.append(apellido)

    id=str(input("Ingresa tu identificacion:\n"))
    while verificacion_id==False:
        tiene_error=False
        for caracteres in id:
            es_un_numero=False
            for num in numeros:
                if caracteres==num:
                    es_un_numero=True
            if es_un_numero==False:
                tiene_error=True
        if tiene_error==True:
            id=str(input("Ingresa tu identificacion correctamente:\n"))
        else:
            verificacion_id=True
            break
    datos_este_empleado.append(id)
    
    edad=int(input("Ingresa tu edad:\n"))
    while verificacion_edad==False:
        if edad<117 and edad>0:
            verificacion_edad=True
        else:
            edad=int(input("Digita tu edad correctamente:\n"))
    datos_este_empleado.append(edad)
            
    tipo=int(input("Ingresa tu tipo de empleado\n(1:OF   2:OP   3:TR):  "))
    while verificacion_tipo==False:
        if tipo==1 or tipo==2 or tipo==3:
            verificacion_tipo=True
        else:
            tipo=int(input("Ingresa tu tipo de empleado correctamente\n(1:OF   2:OP   3:TR):  "))
    datos_este_empleado.append(tipo)


    lista_empleados=[]
    lista_empleados.append(datos_este_empleado)
    return lista_empleados
    

def registrar_ingresos(lista_empleados):
    print("##########-REGISTRAR INGRESO-##########") 
    id_buscar=int("Ingresa el ID del empleado para proceder\n")

    lista_ingreso=[]
    empleado_existe=False
    tipo_empleado=0

    i=0
    while i<len(lista_empleados,lista_ingreso):
        if lista_empleados[i][2]==id_buscar:
            empleado_existe=True
            tipo_empleado=lista_empleados[i][4]
            break
        i=i+1
    if empleado_existe==False:
        print("Usuario Inexistente o no Encontrado...")
        return lista_ingreso
    
    tiene_error=False

    while tiene_error==False:
        fecha_ingresada=int(input("Ingresa la fecha en formato (ddmmyyyy)\n"))
        if fecha_ingresada>10000000 and fecha_ingresada>99999999:
            tiene_error=True
            break
        else:   
            fecha_ingresada=int(input("Ingresa la fecha en formato (ddmmyyyy)\n"))
    
    tiene_error=False
    dia=fecha_ingresada//1000000
    mes=(fecha_ingresada%1000000)//10000
    año=fecha_ingresada%10000
    hora_ingresada=int(input("Ingresa la hora en formato (hhmm)\n"))

    if mes==1:
        if dia<1 or dia>31:
            print("Ingresa los dias en (ddmmyyyy) correctamente\n")
        else:
            if mes==2:
                if dia<1 or dia>28:
                    print("Ingresa los dias en (ddmmyyyy) correctamente\n")
                else:
                    if mes==3:
                        if dia<1 or dia>28:
                            print("Ingresa los dias en (ddmmyyyy) correctamente\n")
                    



    fecha_repetida=False
    j=0
    while j<len(lista_ingreso):



