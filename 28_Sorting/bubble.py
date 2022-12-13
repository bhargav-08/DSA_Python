# Bubble Sort

def bubble(arr):
    flag=1
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                flag=0
                arr[j],arr[j+1]=arr[j+1],arr[j]
        if(flag):break



arr = [14,2,45,19,67]
arr  =[2, 14, 19, 45, 67]
bubble(arr)
print(arr)