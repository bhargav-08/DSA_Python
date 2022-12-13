from queue import Queue
class BinaryTree:
    def __init__(self,data) -> None:
        self.data = data
        self.right = None
        self.left = None
        
def preOrder(root):
    if not root:
        return
    print(root.data)
    preOrder(root.left)
    preOrder(root.right)
    
    
def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print(root.data)
    inOrder(root.right)
    
    
def postOrder(root):
    if not root:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data)

nodes = Queue(0)   

def levelOrder(root):
    if not root:
        return
    print(root.data)
    if root.left or root.right:
        nodes.put(root.left)
        nodes.put(root.right,block=False)
    if not nodes.empty():
        levelOrder(nodes.get(block=False))
        
def levelOrderIterative(root):
    if not root:
        return
    q = Queue(0)
    q.put(root)
   
    while not q.empty():
        root = q.get()
        print(root.data)
        if root.left:
            q.put(root.left)
        if root.right:
            q.put(root.right)

            
  
root = BinaryTree("Drinks")
hot = BinaryTree("Hot")
cold = BinaryTree("Cold")
tea = BinaryTree("Tea")
coffee = BinaryTree("Coffee")
alcoholic = BinaryTree("Alcoholic")
nonalcoholic = BinaryTree("Non-Alcoholic")

root.right = cold
root.left = hot
hot.left = tea
hot.right = coffee
cold.right = alcoholic
cold.left = nonalcoholic

# preOrder(root)
# inOrder(root)
# postOrder(root)  # left right root
# levelOrder(root)
# levelOrderIterative(root)