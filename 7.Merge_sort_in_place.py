def merge(array,start,end):
    
    if start >= end:
        return
    
    mid = (start + end) // 2
    
    merge(array,start,mid)
    merge(array,mid+1,end)
    
    merge_sort(array,mid,start,end)
    
def merge_sort(array,mid,start,end):

    left_array = array[start:mid+1]
    right_array =  array[mid+1:end+1]
    
    l = r = 0
    k =  start
    
    while l< len(left_array) and r < len(right_array):
        if left_array[l] < right_array[r]:
            array[k] = left_array[l]
            l+=1
        else:
            array[k] = right_array[r]
            r+=1
        k+=1
        
    while l < len(left_array):
        array[k] = left_array[l]
        k+=1
        l+=1
    while r < len(right_array):
        array[k] = right_array[r]
        r+=1
        k+=1
    
    print(" ".join(map(str,array)))

arr = [4,1,8,3,0,5,6,2,9]
merge(arr,0,len(arr)-1)
