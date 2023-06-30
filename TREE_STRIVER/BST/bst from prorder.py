class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bstFromPreorder(A):
    def build(val, root):
        if not root:
            root = TreeNode(val)
            return root

        if root.val > val:
            root.left = build(val, root.left)
        else:
            root.right = build(val, root.right)

        return root

    root = None
    for ele in A:
        root = build(ele, root)

    return root


arr = [8, 5, 1, 7, 10, 12]
root = bstFromPreorder(arr)
print(root)
