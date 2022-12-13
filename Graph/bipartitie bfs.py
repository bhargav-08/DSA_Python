# g = {
#     1: [2],
#     2: [1, 3, 8],
#     3: [2, 4],
#     4: [3, 5],
#     5: [8, 6, 4],
#     8: [5, 2],
#     6: [5, 7],
#     7: [6]
# }  # false

g = {
    1: [2],
    2: [1, 3, 8],
    3: [2, 4],
    4: [3, 9],
    5: [8, 6, 9],
    8: [5, 2],
    6: [5, 7],
    7: [6],
    9: [4, 5]
}  # true

import collections


def isBipartite(node):

    color = [-1 for _ in range(len(g) + 1)]

    def helper(node):
        color[node] = 0
        q = collections.deque([node])

        while q:
            node = q.popleft()

            for adj in g[node]:

                if color[adj] == -1:
                    q.append(adj)
                    color[adj] = 1 - color[node]

                elif color[adj] == color[node]:
                    return False

        return True

    return helper(node)


print(isBipartite(1))