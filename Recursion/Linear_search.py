def linear_search(arr,target,index):
    if arr[index] == target:
        return f"The element found at index {index}"
    if index == len(arr)-1:
        return "The element not found"
    return linear_search(arr,target,index+1)

arr = [4,1,2,3,6,7]
target = 3
result = linear_search(arr,target,0)
print(result)