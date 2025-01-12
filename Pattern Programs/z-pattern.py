a=5
for i in range(a,0,-1):
    for j in range(a):
        if i==1 or i==a:
            print("*",end=" ")
        elif i-1 == j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()