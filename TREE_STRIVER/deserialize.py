from collections import deque


class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def deserialize(data):
    """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
    dataq = deque(data.split(","))
    print(dataq)

    def create(dataq):
        if dataq[0] == "None":
            dataq.popleft()
            return None

        node = TreeNode(int(dataq.popleft()))
        node.left = create(dataq)
        node.right = create(dataq)
        return node

    return create(dataq)


def serialize(root):
    """Encodes a tree to a single string.

    :type root: TreeNode
    :rtype: str
    """
    res = []

    def helper(root):
        if not root:
            res.append("None")
            return
        res.append(str(root.val))
        helper(root.left)
        helper(root.right)

    helper(root)
    return ",".join(res)


if __name__ == "__main__":
    s = "1,2,3,None,None,4,5,None,None,None,None"

    root = deserialize(s)
    print(serialize(root))
