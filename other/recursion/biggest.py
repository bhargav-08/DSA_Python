def big(arr):
    if len(arr)==1:
        return arr[0]
    return max(arr[0],big(arr[1:]))


# print(big([10,23,180,90]))

for i in range(9,10):
    print(i)