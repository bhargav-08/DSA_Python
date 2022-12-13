def binarySearch(arr,element,start,end):
    mid = (start+end)//2
    
    if start>end:
        return "Element not present"
    
    if arr[mid]==element:
        return mid
    
    elif arr[mid]>element:
        return binarySearch(arr,element,start,mid-1)

    return binarySearch(arr,element,mid+1,end)
    
    
print(binarySearch([10,20,44,55,60,290],240,0,6))
