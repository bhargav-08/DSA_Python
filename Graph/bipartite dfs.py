g = {
    1: [2],
    2: [1, 3, 8],
    3: [2, 4],
    4: [3, 5],
    5: [8, 6, 4],
    8: [5, 2],
    6: [5, 7],
    7: [6]
}  # false

# g = {
#     1: [2],
#     2: [1, 3, 8],
#     3: [2, 4],
#     4: [3, 9],
#     5: [8, 6, 9],
#     8: [5, 2],
#     6: [5, 7],
#     7: [6],
#     9: [4, 5]
# }  # true

color = [-1 for _ in range(len(g) + 1)]


def isBarpatite(node):

    def helper(node):

        if color[node] == -1:
            color[node] = 1

        for adj in g[node]:
            if color[adj] == -1:
                color[adj] = 1 - color[node]
                if not helper(adj):
                    return False
                
            if color[adj] == color[node]:
                return False
        return True

    return helper(node)


print(isBarpatite(1))
print(color)
