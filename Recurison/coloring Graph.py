def colorNode(N, M, graph):
    color = [-1] * N

    def isValidColor(node, c):

        # adjacent = filter(lambda i,n: , enumerate(graph[node]))
        for adj in adjacent:
            if color[adj] == c:
                return False
        return True

    def solve(node):
        if node == N:
            return True

        for c in range(M):
            if isValidColor(node, c):
                color[node] = c
                if solve(node + 1):
                    return True
                color[node] = -1
        return False

    return solve(0)


N = 4
M = 3
E = 5
edges = [[0 for _ in range(N)] for _ in range(N)]
# for i in range(2 * E):
#     vertexs = input().split()
#     vertexs = list(map(int, vertexs))
#     edges[vertexs[0]][vertexs[1]] = 1

edges = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]

# E = {0: [1, 2, 3], 1: [0, 2], 2: [0, 1, 3], 3: [0, 2]}
# print(colorNode(N, M, edges))

filt = [1, 0, 1, 0, 0, 1]

adjacent = filter(bool, filt)
for adj in adjacent:
    print(adj)
