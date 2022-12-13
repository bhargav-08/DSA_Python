from bfs import g

print(g)
visited = set()


def dfs(n):
    visited.add(n)
    print(n)
    for adjacent in g[n]:
        if adjacent not in visited:
            visited.add(adjacent)
            dfs(adjacent)


dfs("A")