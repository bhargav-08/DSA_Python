from queue import Queue
class BST:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None
        
def insertNode(rootNode,nodeValue):
    if rootNode.data ==None:
        rootNode.data = nodeValue
    elif rootNode.data >= nodeValue:
        if not rootNode.left:
            rootNode.left = BST(nodeValue)
        else:
            insertNode(rootNode.left,nodeValue)
    elif rootNode.data < nodeValue:
        if not rootNode.right:
            rootNode.right = BST(nodeValue)
        else:
            insertNode(rootNode.right,nodeValue)
    return "Successfully inserted Node"
    
def preOrder(root):
    if not root:
        return 
    print(root.data,end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
def inOrder(root):
    if not root:
        return 
    inOrder(root.left)
    print(root.data,end=" ")
    inOrder(root.right)
    
def postOrder(root):
    if not root:
        return 
    postOrder(root.left)
    postOrder(root.right)
    print(root.data,end=" ")
    
def levelOrder(root):
    if not root.data:
        return "Empty Tree!!"
    
    q = Queue()
    q.put(root)
    
    while not q.empty():
        rootValue = q.get()
        print(rootValue.data,end=" ")
        if rootValue.left:
            q.put(rootValue.left)
        if rootValue.right:
            q.put(rootValue.right)
            
def search(root,value):
    if  root.data==value:
        print("Element is Present!!") 
        return root
    
    elif root.data >= value:
        if not root.left:
            print( "Element Not Found")
        else:
            search(root.left,value)
        
    elif root.data < value:
        if not root.right:
            print("Element Not Found")
        else:
            search(root.right,value)

def minValue(root):
    while root.left is not None:
        root = root.left
    return root
      
def deleteNode(root,value):
    if root is None:
        return root
    if root.data > value:
        root.left = deleteNode(root.left,value)
    elif root.data < value:
        root.right = deleteNode(root.right,value)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        if root.right is None:
            temp = root.left
            root= None
            return temp
        
        temp = minValue(root.right)
        root.data = temp.data
        root.right = deleteNode(root.right,temp.data)
    return root
       

def deleteEntire(root):
    root.data = None
    root.left= None
    root.right= None
    return "Successfully Deleted Tree!!"
    
root = BST(None)
insertNode(root,87)
insertNode(root,12)
insertNode(root,67)
insertNode(root,1)
insertNode(root,120)
insertNode(root,116)
# search(root,1)
levelOrder(root)
print()
deleteNode(root,87)
levelOrder(root)

