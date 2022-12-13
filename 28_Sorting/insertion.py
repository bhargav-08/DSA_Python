

from bisect import insort_right


def insertion(arr):
    for i in range(1,len(arr)-1):
        j = i-1
        temp = arr[i]

        while temp < arr[j] and j>=0:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = temp

arr = [14,2,45,2,19,67,68,0,190]
insertion(arr)
print(arr)

