from queue import Queue

class AVLTree:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right= None
        self.height = 1

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

def getHeight(root):
    if not root:
        return 0
    return root.height


def rightRotate(unbalancedNode):
    newRoot = unbalancedNode.left
    unbalancedNode.left = unbalancedNode.left.right
    newRoot.right = unbalancedNode
    unbalancedNode.height =1+max(getHeight(unbalancedNode.left),getHeight(unbalancedNode.right))
    newRoot.height =1+max(getHeight(newRoot.left),getHeight(newRoot.right))
    return newRoot


def leftRotate(unbalancedNode):
    newRoot = unbalancedNode.right
    unbalancedNode.right = unbalancedNode.right.left
    newRoot.left = unbalancedNode
    unbalancedNode.height =1+max(getHeight(unbalancedNode.left),getHeight(unbalancedNode.right))
    newRoot.height =1+max(getHeight(newRoot.left),getHeight(newRoot.right))
    return newRoot


def getBalance(root):
    if not root:
        return 0
    return getHeight(root.left)-getHeight(root.right)

def insertNode(root,nodeValue):
    if not root:
        return AVLTree(nodeValue)
    elif root.data > nodeValue:
        root.left = insertNode(root.left,nodeValue)
    else:
        root.right = insertNode(root.right,nodeValue)

    root.height = 1 + max(getHeight(root.left),getHeight(root.right))
    balance = getBalance(root)

    if balance > 1 and root.left.data > nodeValue :
        return rightRotate(root)
    if balance > 1 and root.left.data < nodeValue :
        root.left = leftRotate(root.left)
        return rightRotate(root)
    if balance < -1 and root.right.data < nodeValue :
        return leftRotate(root)
    if balance < -1 and root.right.data > nodeValue :
        root.right = rightRotate(root.right)
        return leftRotate(root)
    return root

def _getMinValue(root):
    if  root.left is None:
        return root
    return _getMinValue(root.left)

def deleteNode(root,value):
    if not root:
        return root
    elif root.data > value:
        root.left = deleteNode(root.left,value)
    elif root.data < value:
        root.right = deleteNode(root.right,value)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = _getMinValue(root.right)
        root.data=  temp.data
        root.right = deleteNode(root.right,temp.data)

    balance = getBalance(root)

    if balance > 1 and getBalance(root.left) >= 0 :
        return rightRotate(root)
    if balance < -1 and getBalance(root.right) <= 0 :
        return leftRotate(root)
    if balance > 1 and getBalance(root.left) < 0 :
        root.left = leftRotate(root.left)
        return rightRotate(root)
    if balance < -1 and getBalance(root.right) > 0 :
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root

def deleteAVL(rootNode):
    rootNode.data = None
    rootNode.left = None
    rootNode.right = None
    return "The AVL has been successfully deleted"


# avl= AVLTree(78)
# avl = insertNode(avl,10)
# avl = insertNode(avl,15)
# avl = insertNode(avl,20)
# avl = deleteNode(avl,10)

root = AVLTree(30)
# insert(root,30)
root =insertNode(root,25)
root =insertNode(root,35)
root =insertNode(root,20)
root =insertNode(root,15)
root =insertNode(root,5)
root =insertNode(root,10)
root =insertNode(root,50)
root =insertNode(root,60)
root =insertNode(root,70)
root =insertNode(root,65)
levelOrder(root)  # 20 10 50 5 15 30 65 25 35 60 70
deleteNode(root,20)
print()
levelOrder(root)





