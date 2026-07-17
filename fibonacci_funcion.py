def fibonacci(limite):
    a = 0
    b = 1

    print (a)
    
    while b < limite:
        print(b)
        c = a
        a = b
        b = c+b

fibonacci(50)

