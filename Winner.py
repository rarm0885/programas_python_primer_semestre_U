n = int(input())
if n<1 or n>1000:
    print("Type n Correctly...")
else:
    for n in range (0,n):
        name,score = input().split()
        score = int(score)
        if (len(name)<1 or len(name)>32) or (score < -1000 or score > 1000):
            print("Type inputs correctly")
        else:
            