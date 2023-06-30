class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root) -> bool:
    def helper(root, mini, maxi):
        if not root:
            return True

        if mini < root.val < maxi:
            if root.left:
                leftSubTree = helper(root.left, mini, root.val)
            else:
                leftSubTree = True

            if root.right:
                rightSubTree = helper(root.right, root.val, maxi)
            else:
                rightSubTree = True

            return leftSubTree and rightSubTree

    return helper(root, float("-inf"), float("inf"))


root = TreeNode(2, TreeNode(1), TreeNode(3))
print(isValidBST(root))
