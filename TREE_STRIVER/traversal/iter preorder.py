
import sys
sys.path.append("C:\\Users\\bharg\\Desktop\\DSA_Python\\TREE_STRIVER")
from Node import Node
# root left right


def iterPreOrder(root):
    stack = []
    while stack or root:
        while root:
            print(root.val)
            stack.append((root))
            root = root.left

        root = stack.pop()
        root = root.right


root = Node(1, Node(2, Node(3), Node(4, Node(5), Node(6))), Node(7))
iterPreOrder(root)
