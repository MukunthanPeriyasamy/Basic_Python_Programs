a=5
for i in range(1,a+1):
    print(" "*(a-i) + " *"*i,end=" ")
    print()
for i in range(a-1,0,-1):
    print(" "*(a-i) + " *"*i,end=" ")
    print()