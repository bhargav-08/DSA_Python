
import sys
sys.path.append(r"C:\Users\bharg\Desktop\DSA_Python\TREE_STRIVER")
from buildTree import buildTree


class TreeNode:
    def __init__(self, size, mini, maxi):
        self.size = size
        self.mini = mini
        self.maxi = maxi


def largestBst(root):
    def helper(root):
        if not root:
            return TreeNode(0, float("inf"), float("-inf"))

        lh = helper(root.left)
        rh = helper(root.right)

        # Root calculation
        if lh.maxi < root.val < rh.mini:
            return TreeNode(1 + lh.size + rh.size, min(root.val, lh.mini), max(root.val, rh.maxi))

        return TreeNode(max(lh.size, rh.size), float("-inf"), float("inf"))

    return helper(root).size


ip = "1 2 3 N N 4 6 N 5 N N 7 N"

root = buildTree(ip)
print(largestBst(root))
