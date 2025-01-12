def bubbles_sort(arr,index):
    if index==len(arr)-1:
        return arr
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
    return bubbles_sort(arr,index+1)

arr=[9,1,3,6,4,5]
index = 0
result = bubbles_sort(arr,index)
print(result)