
class Node:
    def __init__(self,data) -> None:
        self.data =data
        self.left = None
        self.right = None

def height(root):
    if not root:
        return 0
    if root.left==None and root.right==None:
        return 1
    left = 1 + height(root.left)
    right = 1 + height(root.right)
    return max(left,right)


def isBalanced(root):
    if not root:
        return

    bf = height(root.left) - height(root.right)
    if abs(bf) >1:
        return False
    isBalanced(root.left)
    isBalanced(root.right)
    return True


root = Node(1)
two = Node(2)
three  = Node(3)
four  = Node(4)
five = Node(5)
six  = Node(6)
seven = Node(7)

root.right = three
root.left = two
two.right = five
two.left = four
four.right = six

print('isBalanced(root): ', isBalanced(root))