class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder, inorder):
    inMap = {}
    for idx, val in enumerate(inorder):
        inMap[val] = idx

    def sol(inStart, inEnd, preStart, preEnd):
        if inStart < inEnd or preStart < preEnd:
            return None

        preRoot = inMap[preorder[preStart]]
        leftnode = preRoot - inStart
        root = TreeNode(preorder[preStart])

        root.left = sol(inStart, inStart + leftnode - 1,
                        preStart + 1, preStart + leftnode)
        root.right = sol(preRoot + 1, inEnd, preStart + leftnode + 1, preEnd)
        return root

    return sol(0, len(inorder) - 1, 0, len(preorder))


preOrder = [3, 9, 20, 15, 7]
inOrder = [9, 3, 15, 20, 7]
print(buildTree(preOrder, inOrder))
