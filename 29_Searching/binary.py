

def binary(arr,item):
    start =0
    end= len(arr)-1
    mid = (start+end)//2

    while start <= end:
        if arr[mid]==item:
            return arr.index(item)
        if arr[mid] < item:
            start = mid+1
        if arr[mid] > item:
            end= mid-1
        mid = (start+end)//2
    return -1

arr = [12,34,2,5,6,19,70,45,28]
arr.sort()
print(arr)
print(binary(arr,70))
