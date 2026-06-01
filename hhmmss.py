hhmmss=int(input("Ingresa HHMMSS: "))
hh=hhmmss//10000
mm=(hhmmss%10000)//100
ss=hhmmss%100
if ss<0 or ss>59:
    print("Ingresa bien ss")
if mm<0 or mm>59:
    print("Ingresa bien mm")
if hh<0 or hh>23:
    print("Ingresa bien hh")

ss=ss-1
if ss-1<0:
    ss=59
    mm=mm-1
    if mm-1<0:
        mm=59
        hh=hh-1
        if hh-1<0:
            hh=00
            ss=00
            mm=00



print(hh,mm,ss)

