
class HeapTree:
    def __init__(self,size) -> None:
        self.list = (size+1) * [None]
        self.heapsize = 1
        self.maxsize = size

def inorder(root):
    if root.heapsize==0:
        return "Tree is Empty!!"
    else:
        for i in range(1,root.heapsize):
            print(root.list[i],end=" ")


def heapifyInsert(root,index,type):
    if index<=1:
        return

    parent = index//2

    if type=="Min":
        if root.list[index] < root.list[parent]:
            root.list[index],root.list[parent] = root.list[parent],root.list[index]
        heapifyInsert(root,parent,type)

    elif type=="Max":
        if root.list[index] > root.list[parent]:
            # Interchange
            root.list[index],root.list[parent] = root.list[parent],root.list[index]
        heapifyInsert(root,parent,type)

def insertNode(root,value,type):
    if root.heapsize-1==root.maxsize:
        return "Tree is Full!!"

    root.list[root.heapsize] = value
    heapifyInsert(root,root.heapsize,type)
    root.heapsize+=1

def peekTop(root):
    if not root:
        return
    print(root.list[1])


def sizeOfTree(root):
    return root.heapsize - 1

def extractTopHeapify(root,index,type):
    left = index*2
    right = index*2+1

    if left >= root.heapsize-1:
        return

    elif (root.heapsize-1)==left:
        if type=="Min":
            if root.list[left] < root.list[index]:
                root.list[left],root.list[index] = root.list[index], root.list[left]
            extractTopHeapify(root,left,type)
        if type=="Max":
            if root.list[right] > root.list[index]:
                root.list[right],root.list[index] = root.list[index], root.list[right]
            extractTopHeapify(root,right,type)
    else:
        if type=="Min":
            if left < root.heapsize-1 and root.list[right] > root.list[left] :
                swap = left
            else:
                swap = right
            if  root.list[index] > root.list[swap]:
                root.list[index],root.list[swap]=root.list[swap], root.list[index]
            extractTopHeapify(root,swap,type)

        elif type=="Max":
            if root.list[right] > root.list[left]:
                swap = right
            else:
                swap = left
            if root.list[index] < root.list[swap]:
                root.list[index],root.list[swap]=root.list[swap], root.list[index]
            extractTopHeapify(root,swap,type)

def extractTop(root,type):
    if root.heapsize==0:
        return "Tree is Empty"
    print("\nTop Element is - " + str(root.list[1]))

    root.list[1],root.list[root.heapsize-1] = root.list[root.heapsize-1],root.list[1]
    root.list[root.heapsize-1]=None
    root.heapsize-=1
    extractTopHeapify(root,1,type)

def deleteEntire(root):
    root.list = None

ht = HeapTree(5)
insertNode(ht,4,"Min")
insertNode(ht,5,"Min")
insertNode(ht,11,"Min")
insertNode(ht,2,"Min")
insertNode(ht,1,"Min")
# insertNode(ht,1,"Min")

inorder(ht)
extractTop(ht,"Min")
extractTop(ht,"Min")
# print(sizeOfTree(ht))
inorder(ht)
