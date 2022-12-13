g = {0: [], 1: [], 2: [3], 3: [1], 4: [0, 1], 5: [0, 2]}


def topologicalSort(i):
    vis[i] = 1
    for adj in g[i]:
        if not vis[adj]:
            topologicalSort(adj)
    answer.append(i)


answer = []
vis = [0 for _ in range(len(g))]
for i in range(len(g)):
    if not vis[i]:
        topologicalSort(i)
answer.reverse()
print(answer)