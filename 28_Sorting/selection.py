

def selection(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1,len(arr)-1):
            if arr[min] > arr[j]:
                min=j
        if min!=i:
            arr[i],arr[min]=arr[min],arr[i]
    return arr


if name=="__main__":
    arr = [14,2,45,2,19,67]
    selection(arr)

