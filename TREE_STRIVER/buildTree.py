from collections import deque


class Node:
    def __init__(self, val) -> None:
        self.data = val
        self.right = None
        self.left = None


def buildTree(s):
    if len(s) == 0 or s[0] == "N":
        return None
    ip = list(map(str, s.split()))
    size = 0

    root = Node(int(ip[0]))
    q = deque()
    q.append(root)
    size += 1

    # Start from second element
    i = 1
    while size > 0 and i < len(ip):
        currNode = q.popleft()
        size = size - 1

        currVal = ip[1]

        if currVal != "N":
            currNode.left = Node(int(currVal))

            q.append(currNode.left)
            size += 1
        i += 1

        if (i >= len(ip)):
            break
        currVal = ip[i]

        if currVal != "N":
            currNode.right = Node(int(currVal))

            q.append(currNode.right)
            size += 1
        i += 1

    return root
