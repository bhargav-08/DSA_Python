g = {
    "A": ["B", "C"],
    "B": ["E", "D"],
    "C": ["A", "E"],
    "D": ["E", "F"],
    "E": ["C", "D", "B"],
    "F": ["D", "E"]
}

import collections


def bfs(node):
    visited = set(node)
    q = collections.deque([node])

    while q:
        node = q.popleft()
        print(node)

        for adjacent in g[node]:
            if adjacent not in visited:
                visited.add(adjacent)
                q.append(adjacent)


if __name__ == "__main__":
    bfs("A")
