g = {
    "5": ["2", "6", "8"],
    "2": ["5"],
    "6": ["5"],
    "7": ["8"],
    "8": ["5", "7"],
}


def hasCycle(node):

    visited = set(node)

    def helper(node, parent):
        visited.add(node)

        for adjacent in g[node]:
            if adjacent not in visited:
                visited.add(adjacent)
                return helper(adjacent, node)
            elif adjacent != parent:
                return True
        return False

    return helper(node, -1)


print(hasCycle("2"))