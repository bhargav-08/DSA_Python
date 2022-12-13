# How to find maximum product of two number ?

import numpy as np

arr = np.array([1,2,3,4,5,6,29,27])


def maxProduct(arr):
    product = 0
    for i in range(arr.size):
        for j in range(i+1,arr.size):
            if arr[i]*arr[j] > product:
                num = arr[i],arr[j]
                product = arr[i]*arr[j]
    print(num)
    print(product)
    
def maxProductOn(arr):
    max = 0
    secondmax = 0
    for i in arr:
        if i > max and i >0:
            secondmax,max = max,i
        elif i < max and i > secondmax and i>0:
            secondmax = i 
    print(max,secondmax)
    print(max*secondmax)
    
# maxProduct(arr)
maxProductOn(arr)