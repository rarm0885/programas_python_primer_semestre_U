w=int(input())
if w<1 or w>100:
    print("Your w value is incorrect")
else:
    if w%2==0 and w!=2:
        print("YES")
    else:
        print("NO")