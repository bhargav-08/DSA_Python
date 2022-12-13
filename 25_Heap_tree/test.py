
class HeapTree:
    def __init__(self,maxsize) -> None:
        self.maxsize = maxsize
        self.list = [None]*(self.maxsize+1)
        self.heapsize = 0

def getSize(root):
    return root.heapsize

def peek(root):
    if not root:
        return
    return root.list[1]

def levelOrder(root):
    if not root:
        return

    for i in range(1,root.heapsize+1):
        print(root.list[i],end=" ")

def isFull(root):
    if root.heapsize==root.maxsize:
        return True
    else:
        return False


def heapifyInsert(root,index,type):
    if index <=1:
        return
    parent = index//2

    if root.list[parent]  > root.list[index] and type=="Min":
        root.list[parent],root.list[index] =root.list[index],root.list[parent]
    elif root.list[parent] < root.list[index] and type=="Max":
        root.list[parent],root.list[index] =root.list[index],root.list[parent]

    heapifyInsert(root,parent,type)


def insert(root,value,type):
    if isFull(root):
        return "Tree is Full"

    root.heapsize+=1
    root.list[root.heapsize] = value
    heapifyInsert(root,root.heapsize,type)

def heapifyExtract(root,index,type):

    left=index*2
    right=index*2+1
    min = 0

    if left>root.heapsize or right >root.heapsize:
        return

    if root.list[right] > root.list[left] and type=="Min":
        min = left
    else:
        min=right

    if root.list[min] < root.list[index] and type=="Min":
        root.list[min],root.list[index] = root.list[index],root.list[min]
        heapifyExtract(root,min,type)

    if root.list[right] > root.list[left] and type=="Max":
        min = right
    else:
        min=left

    if root.list[min] > root.list[index] and type=="Max":
        root.list[min],root.list[index] = root.list[index],root.list[min]
        heapifyExtract(root,min,type)


def extractTop(root,type):
    if root.heapsize==0:
        print("Tree is Empty")
        return

    print("Top Element is - " + str(root.list[1]))
    root.list[1]=root.list[root.heapsize]
    root.list[root.heapsize]=None
    root.heapsize-=1
    heapifyExtract(root,1,type)

root =HeapTree(7)
insert(root,10,"Min")
insert(root,30,"Min")
insert(root,20,"Min")
insert(root,80,"Min")
insert(root,40,"Min")
insert(root,50,"Min")
insert(root,60,"Min")
levelOrder(root)
print()
extractTop(root,"Min")
extractTop(root,"Min")
extractTop(root,"Min")
extractTop(root,"Min")
extractTop(root,"Min")
extractTop(root,"Min")
extractTop(root,"Min")
extractTop(root,"Min")

# print(getSize(root))
levelOrder(root)
