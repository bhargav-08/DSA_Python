def eventualSafeNodes(graph):
    V = len(graph)
    safe, path, vis = [], [0 for _ in range(V)], [0 for _ in range(V)]

    def dfs(node):
        path[node] = 1
        vis[node] = 1
        for adj in graph[node]:
            if vis[adj] == 0:
                if dfs(adj):
                    return True
            elif path[adj]:
                return True

        path[node] = 0
        safe.append(node)
        return False

    for i in range(V):
        if not vis[i]:
            dfs(i)

    safe.sort()
    return safe


graph = [[1], [2], [3], [4, 5], [6], [6], [7], [], [1, 9], [10], [8], [9]]
print(eventualSafeNodes(graph))
