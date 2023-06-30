# Definition for a binary tree node.
class TreeNode:
    def __init__(val=0, left=None, right=None):
        val = val
        left = left
        right = right


def hleft(root):
    h = 0
    if not root:
        return h
    while root:
        h += 1
        root = root.left
    return h


def hright(root):
    h = 0
    if not root:
        return h
    while root:
        h += 1
        root = root.right
    return h


def countNodes(root) -> int:
    if not root:
        return 0
    hl = hleft(root)
    hr = hright(root)
    if hl == hr == 1:
        return 1
    if hl == hr:
        return pow(2, hl) - 1
    return 1 + countNodes(root.left) + countNodes(root.right)


root = TreeNode(1)
print(countNodes(root))
