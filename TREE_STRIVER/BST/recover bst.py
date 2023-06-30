from treePrint import printTree

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recoverTree(root) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    def inorder(root):
        nonlocal first, middle, last, prev
        if not root:
            return

        inorder(root.left)
        if prev and prev.val > root.val:
            if first is None:
                first = prev
                middle = root
            else:
                last = root

        prev = root

        inorder(root.right)

    first = middle = prev = last = None

    inorder(root)
    if first and last:
        first.val, last.val = last.val, first.val
    if first and middle:
        first.val, middle.val = middle.val, first.val


root = TreeNode(3, TreeNode(1), TreeNode(4, TreeNode(2)))
print(printTree(root))
recoverTree(root)
print(printTree(root))
