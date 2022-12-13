

def quickSort(arr,start,end):
    if start < end:
        l = partition(arr,start,end)
        quickSort(arr,start,l-1)
        quickSort(arr,l+1,end)

def partition(arr,start,end):
    pivot = start
    front = start
    rear = end

    while front < rear :
        while arr[front] <= arr[pivot] and front <end:
            front+=1

        while arr[rear] > arr[pivot]:
            rear-=1

        if front < rear:
            arr[front],arr[rear] = arr[rear],arr[front]

    arr[pivot],arr[rear] =arr[rear],arr[pivot]
    return rear

"""
def partition(customList, low, high):
    i = low - 1
    pivot = customList[high]
    for j in range(low,high):
        if customList[j] <= pivot:
            i += 1
            customList[i], customList[j] = customList[j], customList[i]
    customList[i+1], customList[high] = customList[high], customList[i+1]
    return (i+1)

def quickSort(customList, low, high):
    if low < high:
        pi = partition(customList, low, high)
        quickSort(customList, low, pi-1)
        quickSort(customList, pi+1, high)
"""


cList = [2,1,7,6,5,3,4,9,8]
quickSort(cList,0,8)
print(cList)