g = {1: [2], 2: [3, 6], 3: [4, 5], 4: [], 5: [4], 6: [7], 7: [8], 8: [6]}


def dfs(node):
    dfsvis = [0 for _ in range(len(g) + 1)]
    vis = [0 for _ in range(len(g) + 1)]

    def helper(node):
        vis[node] = 1
        dfsvis[node] = 1

        for adj in g[node]:

            if vis[adj] == 0:
                helper(adj)

            if dfsvis[adj]:
                return True

        dfsvis[node] = 0
        return False

    return helper(node)


print(dfs(1))