from time import time
from random import randint

def merge(arr,low,mid,high):
    a = low
    b=mid+1
    i = 0
    temp = [None]*(high-low+1)

    while a <= mid and b <= high:
        if arr[a]>arr[b]:
            temp[i] = arr[b]
            i+=1;b+=1;
        else:
            temp[i]=arr[a] # stable
            i+=1;a+=1;

    while a <= mid:
        temp[i] = arr[a]
        a+=1;i+=1;

    while b <= high:
        temp[i] = arr[b]
        b+=1;i+=1;

    arr[low:high+1] = temp


def mergeSort(arr,low,high):
    mid = (high+low)//2

    if low<high:
        mergeSort(arr,low,mid)
        mergeSort(arr,mid+1,high)
        merge(arr,low,mid,high)


arr = [23,1,190,34,189,289,12]
mergeSort(arr,0,len(arr)-1)
print(arr)