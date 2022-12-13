
arr = [[1,2,3],[4,5,6],[7,8,9]]
t = [[0 for i in range(len(arr))] for j in range(len(arr[0]))]


for i in range(len(t)):
    for j in range(len(t[0])):
        t[i][j] = arr[j][i]


for i in range(len(t)):
    t[i].reverse()
    
# print(t)

# print(5//2)

def rotateby90(arr):
    length = len(arr)
    layer = length//2
    for i in range(layer):
        first = i
        last = length-i-1
        for i in range(first,last):
            top = arr[layer][first]
            print(arr[layer][first])
            arr[layer][first] = arr[last-i][-layer-i]
            print(arr[last-i][-layer-i])
            arr[last-i][-layer-i] = arr[-last-i][layer]
            print(arr[-last-i][layer])
            arr[-last-i][layer] = arr[-last-i][-layer-i]
            print(arr[-last-i][-layer-i])
            arr[-layer-i][-last-i] = top
    return arr

print(arr)
print(rotateby90(arr))