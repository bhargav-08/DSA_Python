import math
from  selection import selection as sel

def bucketSort(arr):
    buckets = []
    no_of_bucket = round(math.sqrt(len(arr)))
    for _ in range(no_of_bucket):
        buckets.append([])

    maxValue =  max(arr)

    for i in arr:
        index_b = math.ceil(i*no_of_bucket/maxValue)
        buckets[index_b-1].append(i)

    for i in range(no_of_bucket):
        buckets[i] = sel(buckets[i])

    k=0
    for j in range(no_of_bucket):
        for i in range(len(buckets[j])):
            arr[k] = buckets[j][i]
            k+=1

    return arr

arr = [14,2,45,19,65]
bucketSort(arr)
print('arr: ', arr)
