from queue import Queue
from traversal import BinaryTree,root,levelOrderIterative


def deepestNode(rootNode):
    if not rootNode:
        return
    
    q = Queue()
    q.put(rootNode)
    
    while not q.empty():
        root = q.get()
        if root.left:
            q.put(root.left)
        if root.right:
            q.put(root.right)
    return root


def deleteDeepestNode(rootNode,dNode):
    if not rootNode:
        return
    
    q = Queue()
    q.put(rootNode)
    
    while not q.empty():
        root = q.get()
        if root is dNode:
            root = None
            return 
        
        if root.left:
            if root.left is dNode:
                root.left = None
                return
            else:
                q.put(root.left)
        
        if root.right:    
            if root.right is dNode:
                root.right = None
                return
            else:
                q.put(root.right) 


def deleteNodeBT(rootNode,node):
    if not rootNode:
        return
    
    q = Queue()
    q.put(rootNode)
    
    while not q.empty():
        root = q.get()
        if root.data == node.data:
            dn = deepestNode(rootNode)
            deleteDeepestNode(rootNode,dn)
            root.data = dn.data
            return "Node Successfully Deleted"
        
        if root.left:
            q.put(root.left)    
                           
        if root.right:
            q.put(root.right)               
    
    return "Failed to delete!!"

def deleteEntireBT(root):
    root.left=None
    root.right=None
    root.data=None
    return "Successfully Deleted Binary Tree"

levelOrderIterative(root)
# newNode = deepestNode(root)
# deleteDeepestNode(root,newNode)
print()
node = BinaryTree("Drinks")
# deleteNodeBT(root,node)
deleteEntireBT(root)
levelOrderIterative(root)