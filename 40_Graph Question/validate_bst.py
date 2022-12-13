
import sys


class Node:
    def __init__(self,data,left=None,right=None) -> None:
        self.data = data
        self.left = left
        self.right = right

def bstValidate(root):
    lb = -100000
    ub = sys.maxsize
    if not root:
        return
    return bstHelper(root,lb,ub)

def bstHelper(root,lb,ub):
    if not root:
        return True
    val = root.data
    if val > ub and val <lb:
        return False
    if not bstHelper(root.left,lb,val):
        return False
    if not bstHelper(root.right,root.data,ub):
        return False
    return False

two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)


root= Node(1,two,three)
two.left = four
two.right = five
three.left = six
three.right = seven
print(bstValidate(root))



