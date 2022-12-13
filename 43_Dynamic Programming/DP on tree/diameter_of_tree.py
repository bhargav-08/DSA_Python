class Node:

    def __init__(self, left=None, right=None, value=0) -> None:
        self.left = left
        self.right = right
        self.value = value


root = Node()
n1 = Node()
n2 = Node()
n3 = Node()
n4 = Node()
n5 = Node()
n6 = Node()
n7 = Node()
root.left = n1
root.right = n2
n1.left = n3
n1.right = n4
n2.left = n5
n2.right = n6
n3.left = n7


def diameter(root):
    global res
    if root == None:
        return 0

    l = diameter(root.left)
    r = diameter(root.right)

    temp = max(l, r) + 1
    ans = max(temp, 1 + r + l)
    res = max(ans, res)

    return temp


res = 0
diameter(root)
print(res)
