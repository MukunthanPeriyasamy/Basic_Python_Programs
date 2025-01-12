def linear_search(arr,target,index):
    if index == len(arr) -1:
        return f"Element not found"
    elif arr[index] == target:
        return f"The Element found at index {index}"
    return linear_search(arr,target,index+1)
arr = [3,4,5,1,6,7,8,0]
target = 6
result = linear_search(arr,target,0)
print(result)