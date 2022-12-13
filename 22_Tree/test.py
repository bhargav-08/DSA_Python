
from queue import Queue

class BSTNode:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None
        
def insert(root,value):
    if root.data==None:
        root.data=value
    elif root.data>=value:
        if root.left:
            insert(root.left,value)
        else:
            root.left =  BSTNode(value)
    else:
        if root.right:
            insert(root.right,value)    
        else:
            root.right = BSTNode(value)
    return "Node is Successfully inserted!!"

def search(root,value):
    if not root:
        print("Failure")
        return
    elif root.data==value:
        print("Success")
        return
    elif root.data>=value:
        search(root.left,value)
    elif root.data<value:
        search(root.right,value)
    
# def insert(root,value):
#     if not root:
#         return BSTNode(value)
#     if root.data>=value:
#         root.left = insert(root.left,value)
#     else:
#         root.right = insert(root.right,value)
#     return root

def getNextNode(root):
    if not root:
        return root
    
    while root.left:
        root=root.left
    return root
    

def deleteNode(root,value):
    if not root:
        print("Failure")
        return
    if root.data > value:
        root.left = deleteNode(root.left,value)       
    elif root.data < value:
        root.right = deleteNode(root.right,value)
    else:
        if  root.right is None:
            temp = root.left
            root = None
            return temp
            
        if  root.left is None:
            temp = root.right
            root = None
            return temp
            
        successor = getNextNode(root.right)
        root.data = successor.data
        root.right = deleteNode(root.right,successor.data)
    return root
        
        
def levelOrder(root):
    if not root:
        return
    q = Queue()
    q.put(root)
    
    while not q.empty():
        root = q.get()
        print(root.data)
        if root.left:
            q.put(root.left)
        if root.right:
            q.put(root.right)
            
            
root = BSTNode(10)
insert(root,73)
insert(root,54)
insert(root,7)
insert(root,8)
insert(root,64)
# search(root,8)
levelOrder(root)

deleteNode(root,10)
print("-------------------")
levelOrder(root)





# Creation ,traversal,insertion,searching,deletion