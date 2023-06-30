# Following is the Binary Tree node structure:
class BinaryTreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def isLeaf(node):
    if not node:
        return False
    if node.left is None and node.right is None:
        return True
    return False


def leftBoundary(root, res):
    curr = root.left
    while curr:
        if (not isLeaf(curr)):
            res.append(curr.data)

        if curr.left:
            curr = curr.left
        else:
            curr = curr.right


def leafTraversal(root, res):
    if not root:
        return
    if (isLeaf(root)):
        res.append(root.data)

    leafTraversal(root.left, res)
    leafTraversal(root.right, res)


def rightBoundary(root, res):
    level = []
    curr = root.right
    while curr:
        if (not isLeaf(curr)):
            level.append(curr.data)
        if (curr.right):
            curr = curr.right
        else:
            curr = curr.left

    for i in range(len(level) - 1, -1, -1):
        res.append(level[i])


def traverseBoundary(root):
    # Write your code here.
    res = []
    if not root:
        return root
    if (not isLeaf(root)):
        res.append(root.data)
    leftBoundary(root, res)
    leafTraversal(root, res)
    rightBoundary(root, res)
    return res


root = BinaryTreeNode(1, BinaryTreeNode(2, BinaryTreeNode(
    4, None, BinaryTreeNode(7))), BinaryTreeNode(3, BinaryTreeNode(5), BinaryTreeNode(6)))

print(traverseBoundary(root))
