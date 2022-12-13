def linear(arr,item):
    for i in arr:
        if i==item:
            return arr.index(i)
    return -1

arr = [12,34,2,5,6,19,70,45,28]
print(linear(arr,6))