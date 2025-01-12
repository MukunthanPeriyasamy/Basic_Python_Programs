def merge_sort(arr):
    
    if len(arr) ==1 :
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left,right)
    

def merge(left,right):
    l = 0
    r = 0
    k = 0
    
    """ Initializing 0's for the length of both left and right list to `assign` the values to the mix list. 
    we can also initlize the list as empty and use append method to add the values to the list."""
    
    mix = [0] * (len(left) + len(right))
    
    while l<len(left) and r< len(right):
        if left[l] <= right[r]:
            mix[k] = left[l]
            l+=1
        else:
            mix[k] = right[r]
            r+=1
        k+=1
    while l < len(left):
        mix[k] = left[l]
        l+=1
        k+=1
    while r< len(right):
        mix[k] = right[r]
        r+=1
        k+=1
    return mix

arr = [1,6,2,2,8,3,0,-1]
result = merge_sort(arr)
print(result)
