def binary_search(arr,target,low,high):
    
    mid = low + (high - low) // 2
    
    if arr[mid] == target:
        return f"Element found at index {mid}"
    elif low > high:
        return f"Element not found"
    elif arr[mid] > target:
        return binary_search(arr,target,low,mid-1)
    else:
        return binary_search(arr,target,mid+1,high)
arr = [1,2,3,4,5,6,7]
target = 8
result = binary_search(arr,target,0,len(arr)-1)
print(result)