a = 5
for i in range(1,a+1):
    print("*",end=" ")
    for j in range(2,i+1):
        if j==i:
            print("*",end=" ")
        elif i==a:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()