def mcm (num2,num1):
    if num2 == 0:
        return num1
    else:
        return mcm(num1%num2,num2)

print(mcm(48,18))
