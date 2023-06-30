class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


from collections import deque


def distanceK(root: TreeNode, target: TreeNode, k: int):
    par = {}
    q = deque([root])
    # Get the parent node of all nodes
    while q:
        size = len(q)
        for _ in range(size):
            node = q.popleft()
            if node.left:
                par[node.left] = node
                q.append(node.left)
            if node.right:
                par[node.right] = node
                q.append(node.right)

    # Calculate all node at distance of k
    q = deque([target])
    vis, dist = set(), 0
    while q:
        size = len(q)
        if dist == k:
            return [node.val for node in q]
        for _ in range(size):
            node = q.popleft()
            vis.add(node)
            if node.left and node.left not in vis:
                q.append(node.left)
            if node.right and node.right not in vis:
                q.append(node.right)
            if par.get(node, 0) and par.get(node, 0) not in vis:
                q.append(par.get(node))
        # print(q)
        dist += 1


root = TreeNode(3, left=TreeNode(5, left=TreeNode(6, left=None, right=None), right=TreeNode(2, left=TreeNode(7, left=None, right=None), right=TreeNode(
    4, left=None, right=None))), right=TreeNode(1, left=TreeNode(0, left=None, right=None), right=TreeNode(8, left=None, right=None)))

root = TreeNode(1)
ans = distanceK(root, root, 3)
print(ans)
