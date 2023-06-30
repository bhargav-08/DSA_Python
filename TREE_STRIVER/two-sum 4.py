class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findTarget(root, k):
    if not root:
        return False
    bfs, s = [root], set()
    for i in bfs:
        if k - i.val in s:
            return True
        s.add(i.val)
        if i.left:
            bfs.append(i.left)
        if i.right:
            bfs.append(i.right)
    return False


root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)),
                TreeNode(6, None, TreeNode(7)))
print(findTarget(root, 9))
