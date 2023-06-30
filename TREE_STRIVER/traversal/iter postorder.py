import sys
sys.path.append("C:\\Users\\bharg\\Desktop\\DSA_Python\\TREE_STRIVER")
from Node import Node


def iterPostOrder(root):
    stack, res = [root], []
    while stack:
        root = stack.pop()
        res.append(root.val)
        if root.left:
            stack.append(root.left)
        if root.right:
            stack.append(root.right)

    return res[::-1]


root = Node(1, Node(2, Node(3), Node(4, Node(5), Node(6))), Node(7))
print(iterPostOrder(root))
