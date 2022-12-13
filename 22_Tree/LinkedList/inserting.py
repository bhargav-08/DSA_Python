
from queue import Queue
from traversal import BinaryTree,root,levelOrderIterative


def insertNodeBT(rootNode,newNode):
    if not rootNode:
        rootNode = rootNode
    else:
        q = Queue()
        q.put(rootNode)
        
        while not q.empty():
            root = q.get()
            if root.left:
                q.put(root.left)
            else:
                root.left = newNode
                return "Successfully Inserted"
                
            if root.right:
                q.put(root.right)
            else:
                root.right = newNode
                return "Successfully Inserted"


newNode = BinaryTree("Cola")
newNode1 = BinaryTree("Cola1")
newNode2 = BinaryTree("Cola2")
newNode3 = BinaryTree("Cola3")
newNode4 = BinaryTree("Cola4")
print(insertNodeBT(root,newNode))
levelOrderIterative(root)