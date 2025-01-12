def selection_sort(arr,index):
    if index==len(arr)-1:
        return arr
    min = index 
    
    for i in range(index+1,len(arr)):
        j=arr[i]
        if arr[min] > j:
            min = i
    arr[min],arr[index] = arr[index],arr[min]
    return selection_sort(arr,index+1)

arr = [1,6,2,3,8,0,34,12,-1]
index=0
result = selection_sort(arr,index)
print(result)
