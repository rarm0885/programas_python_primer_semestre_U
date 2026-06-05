def crear_empleado(lista_empleados):
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
            verificacion_apellido=True
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

    lista_empleados.append(datos_este_empleado)
    print("Empleado ingresado con exito!!!")
    return lista_empleados

def registrar_ingresos(lista_empleados,lista_ingreso):
    print("##########-REGISTRAR INGRESO-##########") 
    id_buscar=str(input("Ingresa el ID del empleado para proceder\n"))

    empleado_existe=False
    tipo_empleado=0

    i=0
    while i<len(lista_empleados):
        if lista_empleados[i][2]==id_buscar:
            empleado_existe=True
            tipo_empleado=lista_empleados[i][4]
            break
        i=i+1
    if empleado_existe==False:
        print("Usuario Inexistente o no Encontrado...")
        return lista_ingreso
    
    while True:
        fecha_ingresada=int(input("Ingresa la fecha en formato (ddmmyyyy)\n"))
        if fecha_ingresada>=1000000 and fecha_ingresada<=99999999:
            dia=fecha_ingresada//1000000
            mes=(fecha_ingresada%1000000)//10000
            año=fecha_ingresada%10000
            
            fecha_valida=True
            
            if mes<1 or mes>12:
                print("El mes ingresado no existe. Intentalo de nuevo")
                fecha_valida=False
            elif mes%2==0 and mes!=2:
                if dia>30 or dia<=0:
                    print("Ingresa bien el dia dentro de tu fecha (ddmmyyyy)")
                    fecha_valida=False
            elif mes==2:
                if dia>29 or dia<=0:
                    print("Ingresa bien el dia dentro de tu fecha (ddmmyyyy)")
                    fecha_valida=False
            else:
                if dia>31 or dia<=0:
                    print("Ingresa bien el dia dentro de tu fecha (ddmmyyyy)")
                    fecha_valida=False
            
            if fecha_valida==True:
                break
        else:
            print("Cantidad de numeros incorrecta... Intentalo de nuevo")
    
    fecha_repetida=False
    j=0
    while j<len(lista_ingreso):
        if lista_ingreso[j][0]==id_buscar and lista_ingreso[j][1]==fecha_ingresada:
            fecha_repetida=True
            break
        j=j+1
    if fecha_repetida==True:
        print("ERROR Este empleado ya fue registrado el dia de hoy...")
        return lista_ingreso
    
    while True:
        hora_ingresada=int(input("Ingresa la hora en formato (hhmm)\n"))
        if (hora_ingresada//100>23 or hora_ingresada//100<0) or (hora_ingresada%100<0 or hora_ingresada%100>59):
            print("Ingrese la hora correctamente:")
        else:
            break
    
    hora=hora_ingresada//100
    minuto=hora_ingresada%100

    llego_tarde="No"
    if tipo_empleado==1:
        if hora>9 or (hora==9 and minuto>0):
            llego_tarde="Si"
    elif tipo_empleado==2:
        if hora>7 or (hora==7 and minuto>30):
            llego_tarde="Si"
    elif tipo_empleado==3:
        if hora>6 or (hora==6 and minuto>0):
            llego_tarde="Si"

    datos_este_ingreso=[id_buscar,fecha_ingresada,hora_ingresada,llego_tarde]
    lista_ingreso.append(datos_este_ingreso)
    
    print(f"¡Ingreso registrado exitosamente! ¿Llegó tarde?:  {llego_tarde}")
    return lista_ingreso

def mostrar_todos(lista_empleados,lista_ingresos):
    print("----Todos los ingresos----")
    j=0
    while j<len(lista_ingresos):
        id_ingreso =lista_ingresos[j][0]
        fecha=lista_ingresos[j][1]
        hora=lista_ingresos[j][2]

        i=0
        while i<len(lista_empleados):
            if lista_empleados [i][2] == id_ingreso:
                nombre=lista_empleados[i][0]
                apellido=lista_empleados[i][1]

                print('"'+ nombre +','+ apellido +','+ id_ingreso + ',' + str(fecha) + ',' + str(hora) + '"')
                break
            i=i+1
        j=j+1

def mostrar_tarde(lista_empleados,lista_ingresos):
    print("---INGRESOS TARDE---")
    j=0
    while j<len(lista_ingresos):
        if lista_ingresos[j][3]=="Si":
            id_ingreso=lista_ingresos[j][0]
            fecha=lista_ingresos[j][1]
            hora=lista_ingresos[j][2]

            i=0
            while i<len(lista_empleados):
                if lista_empleados[i][2]==id_ingreso:
                    nombre=lista_empleados[i][0]
                    apellido=lista_empleados[i][1]
                    print('"' + nombre + '","' + apellido + '","' + id_ingreso + '","' + str(fecha) + '","' + str(hora) + '"')
                    break
                i=i+1
        j=j+1

def mostrar_of(lista_empleados,lista_ingresos):
    print("----INGRESOS DE OFICINA (OF)----")
    j=0
    while j<len(lista_ingresos):
        id_ingreso=lista_ingresos[j][0]
        fecha=lista_ingresos[j][1]
        hora=lista_ingresos[j][2]

        i=0
        while i<len(lista_empleados):
            if lista_empleados[i][2]==id_ingreso:
                if lista_empleados[i][4]==1:
                    nombre=lista_empleados[i][0]
                    apellido=lista_empleados[i][1]
                    print('"' + nombre + '","' + apellido + '","' + id_ingreso + '","' + str(fecha) + '","' + str(hora) + '"')
                break
            i=i+1
        j=j+1

def mostrar_op(lista_empleados,lista_ingresos):
    print("----INGRESOS DE OPERARIOS (OP)----")
    j=0
    while j<len(lista_ingresos):
        id_ingreso=lista_ingresos[j][0]
        fecha=lista_ingresos[j][1]
        hora=lista_ingresos[j][2]

        i=0
        while i<len(lista_empleados):
            if lista_empleados[i][2]==id_ingreso:
                if lista_empleados[i][4]==2:
                    nombre=lista_empleados[i][0]
                    apellido=lista_empleados[i][1]
                    print('"' + nombre + '","' + apellido + '","' + id_ingreso + '","' + str(fecha) + '","' + str(hora) + '"')
                break
            i=i+1
        j=j+1

def mostrar_tr(lista_empleados,lista_ingresos):
    print("----INGRESOS DE TRANSPORTE (TR)----")
    j=0
    while j<len(lista_ingresos):
        id_ingreso=lista_ingresos[j][0]
        fecha=lista_ingresos[j][1]
        hora=lista_ingresos[j][2]

        i=0
        while i<len(lista_empleados):
            if lista_empleados[i][2]==id_ingreso:
                if lista_empleados[i][4]==3:
                    nombre=lista_empleados[i][0]
                    apellido=lista_empleados[i][1]
                    print('"' + nombre + '","' + apellido + '","' + id_ingreso + '","' + str(fecha) + '","' + str(hora) + '"')
                break
            i=i+1
        j=j+1

def menu_principal():
    mis_empleados=[]
    mis_ingresos=[]
    
    ejecutar_menu=True

    while ejecutar_menu==True:
        print("\n----MENU PRINCIPAL (NOMBRE EMPRESA)----")
        print("1. Crear empleado")
        print("2. Registrar Ingreso")
        print("3. mostrar todos los ingresos")
        print("4. Mostrar quienes llegaron tarde")
        print("5. Mostrar todos los ingresos de OF")
        print("6. Mostrar todos los ingresos de OP")
        print("7. Mostrar todos los ingresos de TR")
        print("8. Salir")

        opcion=int(input("\nIngresa una opcion:\n"))

        if opcion==1:
            mis_empleados=crear_empleado(mis_empleados)
        elif opcion==2:
            mis_ingresos=registrar_ingresos(mis_empleados,mis_ingresos)
        elif opcion==3:
            mostrar_todos(mis_empleados,mis_ingresos)
        elif opcion==4:
            mostrar_tarde(mis_empleados,mis_ingresos)
        elif opcion==5:
            mostrar_of(mis_empleados,mis_ingresos)
        elif opcion==6:
            mostrar_op(mis_empleados,mis_ingresos)
        elif opcion==7:
            mostrar_tr(mis_empleados,mis_ingresos)
        elif opcion==8:
            print("saliendo del programa...")
            ejecutar_menu=False
        else:
            print("Opcion no valida, Intentalo de nuevo...\n")

menu_principal()
