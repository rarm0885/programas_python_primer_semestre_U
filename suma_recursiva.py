def suma (numero):
    if numero == 1:
        return 1
    else:
        return numero + suma (numero - 1)



def suma_digitos (numero):
    if numero == 0:
        return 0
    else:
        return numero % 10 + suma_digitos(numero//10)


def cuenta_regresiva (n):
    if n == 0:
        return 0

    print(n,end=",")
    return cuenta_regresiva(n-1)


def cuenta_progresiva(n):
    if n == 0:
        return 0
    else:
        cuenta_progresiva(n-1)
        print(n,end = " ")

cuenta_progresiva(5)