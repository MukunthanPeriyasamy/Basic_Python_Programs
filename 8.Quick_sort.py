def quickSort(arr):
    if len(arr) <=1:
        return arr
    
    pivot = len(arr) // 2
    pivot = arr[pivot]
    
    left = [i for i in arr if i < pivot]
    right = [i for i in arr if i > pivot]
    middle = [i for i in arr if i == pivot]
    
    mix = left + middle + right
    print(" ".join(map(str,mix)))
    return quickSort(left) + middle + quickSort(right)

arr = [3,1,2,7,4,8,9,0]
result = quickSort(arr)
print(result)