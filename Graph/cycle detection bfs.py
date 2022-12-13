g = {
    "3": ["5"],
    "5": ["3", "6", "10"],
    "6": ["5", "7", "8"],
    "7": ["6"],
    "10": ["5", "9"],
    "9": ["10", "8"],
    "8": ["9", "11", "7"],
    "11": ["8"]
}
import collections


def cycleBFS(node):
    visited = set(node)
    q = collections.deque()
    q.append((node, -1))

    while q:
        node = q.popleft()
        for adjacent in g[node[0]]:
            if adjacent not in visited:
                visited.add(adjacent)
                q.append((adjacent, node[0]))
            elif node[1] != adjacent:
                return True

    return False


print(cycleBFS("3"))
