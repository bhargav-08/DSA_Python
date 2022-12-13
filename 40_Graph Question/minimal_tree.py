
class Node:
    def __init__(self,data,left=None,right=None) -> None:
        self.data= data
        self.left =None
        self.right =None

def sortedArray(arr):
    if len(arr)==0:
        return None
    if len(arr)==1:
        return Node(arr[0])
    mid = len(arr)//2
    left = sortedArray(arr[:mid])
    right = sortedArray(arr[mid+1:])
    return Node(arr[mid],left,right)

arr = [1,2,3,4,5,6]
bst = sortedArray(arr)
print(bst.data)
