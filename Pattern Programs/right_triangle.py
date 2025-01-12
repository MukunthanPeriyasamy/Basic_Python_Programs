a = 5
for i in range(1,a+1):
    for j in range((a-i)):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()    