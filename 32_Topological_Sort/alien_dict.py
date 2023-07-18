from collections import defaultdict, deque


def findOrder(alien_dict, N, K):
    # code here
    graph = defaultdict(list)
    indegree = [0] * K

    for w1, w2 in zip(alien_dict, alien_dict[1:]):
        i, j = 0, 0
        while i < len(w1) and j < len(w2):
            if w1[i] != w2[j]:
                graph[ord(w1[i]) - 97].append(ord(w2[j]) - 97)
                indegree[ord(w2[j]) - 97] += 1
                break
            i += 1
            j += 1

    # Topo sort
    q = deque()
    topo = []

    for idx, val in enumerate(indegree):
        if val == 0:
            q.append(idx)

    while q:
        node = q.popleft()
        topo.append(chr(node + 65))
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    return topo


ad = ["baa", "abcd", "abca", "cab", "cada", ]
k = 5
n = 4
print(findOrder(ad, k, n))
