# multiple occurence of the target value 
def linear_search(arr,target,index,lis):
    if index == len(arr):
        return lis
    elif arr[index] == target:
        lis.append(index)
    return linear_search(arr,target,index+1,lis)
arr = [3,4,5,1,6,7,8,0,6]
target = 6
result = linear_search(arr,target,0,[])
if result:
    print(f"The Element is found at {"".join(str(result))}")
else:
    print("The Element is not found")