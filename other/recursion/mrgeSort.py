

def merge(arr,start,mid,end):
    i = start
    j=mid+1
    k=0
    temp = [None]*(end-start+1)
    
    while i<=mid and j<=end:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i+=1;k+=1;
        else:
            temp[k] =arr[j]
            j+=1;k+=1;
    
    while i<=mid:
        temp[k] = arr[i]
        k+=1;i+=1;
        
    while j<=end:
        temp[k] = arr[j]
        k+=1;j+=1;
    
    arr[start:end+1] = temp 

def mergeSort(arr,start,end):
    if start <end:
        mid = (start+end)//2

        mergeSort(arr,start,mid)
        mergeSort(arr,mid+1,end)
        merge(arr,start,mid,end)
       
l = [108,23,2,19,56,190]
mergeSort(l,0,5)
print(l)