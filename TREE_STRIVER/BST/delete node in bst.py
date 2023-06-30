
from treePrint import printTree


class TreeNode():
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def deleteNode(root, key: int):
    def findRightMost(root):
        while root.right:
            root = root.right
        return root

    def helper(root):
        if not root.left:
            return root.right

        rightChild = findRightMost(root.left)
        rightChild.right = root.right
        return root.left

    if not root:
        return root
    curr = root
    if root.val == key:
        return helper(root)

    while root:
        if root.val > key:
            if root.left and root.left.val == key:
                root.left = helper(root.left)
                return curr
            else:
                root = root.left
        else:
            if root.right and root.right.val == key:
                root.right = helper(root.right)
                return curr
            else:
                root = root.right

    return curr


root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)),
                TreeNode(6, None, TreeNode(7)))
root = deleteNode(root, 3)

print(printTree(root))
