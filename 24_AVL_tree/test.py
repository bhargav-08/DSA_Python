from logging import RootLogger
from queue import Queue

class AVLTree:
    def __init__(self,data) -> None:
        self.data =data
        self.right = None
        self.left = None
        self.height = 1

def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print(root.data,end=" ")
    inOrder(root.right)

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

def getBalance(root):
    return (getHeight(root.left)-getHeight(root.right))

def rightRotate(unbalanced):
    newRoot =  unbalanced.left
    unbalanced.left = unbalanced.left.right
    newRoot.right = unbalanced

    # update height of unbalance and root
    unbalanced.height = 1 + max(getHeight(unbalanced.right),getHeight(unbalanced.left))
    newRoot.height = 1 + max(getHeight(newRoot.right),getHeight(newRoot.left))
    return newRoot

def leftRotate(unbalanced):
    newRoot =  unbalanced.right
    unbalanced.right = unbalanced.right.left
    newRoot.left = unbalanced

    # update height of unbalance and root
    unbalanced.height = 1 + max(getHeight(unbalanced.left),getHeight(unbalanced.right))
    newRoot.height = 1 + max(getHeight(newRoot.left),getHeight(newRoot.right))
    return newRoot

def insert(root,value):
    if not root:
        return AVLTree(value)
    elif root.data >= value:
        root.left = insert(root.left,value)
    elif root.data < value:
        root.right = insert(root.right,value)

    root.height = 1 + max(getHeight(root.left),getHeight(root.right))
    balance = getBalance(root)

    if balance > 1 and getBalance(root.left)>=0:
        return rightRotate(root)
    if balance >1 and getBalance(root.left)<0:
        root.left = leftRotate(root.left)
        return rightRotate(root)
    if balance < -1 and getBalance(root.right) <= 0:
        return leftRotate(root)
    if balance < -1 and getBalance(root.right) > 0:
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root

def getSuccessor(root):
    if root.left is None:
        return root
    else:
        return getSuccessor(root.left)

def deleteNode(root,value):
    if not root:
         return root

    if root.data > value:
        root.left = deleteNode(root.left,value)

    elif root.data < value:
        root.right = deleteNode(root.right,value)

    else:
        if root.left is None:
            temp =root.right
            root=None
            return temp

        elif root.right is None:
            temp = root.left
            root= None
            return temp

        temp = getSuccessor(root.right)
        # print(temp.data)
        root.data = temp.data
        root.right = deleteNode(root.right,temp.data)

    balance = getBalance(root)

    if balance > 1 and getBalance(root.left)>=0:
        return rightRotate(root)
    if balance >1 and getBalance(root.left)<0:
        root.left = leftRotate(root.left)
        return rightRotate(root)
    if balance < -1 and getBalance(root.right) <= 0:
        return leftRotate(root)
    if balance < -1 and getBalance(root.right) > 0:
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root



root = AVLTree(30)
# insert(root,30)
root = insert(root,25)
root = insert(root,35)
root = insert(root,20)
root = insert(root,15)
root = insert(root,5)
root = insert(root,10)
root = insert(root,50)
root = insert(root,60)
root = insert(root,70)
root = insert(root,65)
levelOrder(root)
deleteNode(root,600)
print()
levelOrder(root)