
# def djisktra(graph, source):
#     V = len(graph)
#     vis = [False]*V
#     val = [float("inf")]*V
#     parent = [-1]*V

#     def selectMinVertex():
#         node, minVal = -1, float("inf")

#         for i in range(V):
#             if not vis[i] and val[i] < minVal:
#                 node = i
#                 minVal = val[i]

#         return node

#     # setting source as min val and its parent
#     val[source] = 0
#     parent[source] = -1

#     for i in range(V):
#         U = selectMinVertex()
#         vis[U] = True

#         # relaxing edges
#         for j in range(V):
#             if not vis[j] and graph[U][j] != 0 and val[j] > val[U]+graph[U][j]:
#                 val[j] = val[U]+graph[U][j]
#                 parent[j] = U

#     # Print the val
#     print(f"{val= }")
#     print(f"{parent= }")


from heapq import heappop, heappush


def djisktra(graph, source):
    V = len(graph)
    vis = [False]*V
    val = [float("inf")]*V
    parent = [-1]*V

    # setting source as min val and its parent
    val[source] = 0
    parent[source] = -1
    pq = []
    heappush(pq, (0, source))

    while pq:
        U, dist = heappop(pq)

        # relaxing edges
        if not vis[U]:
            for j in range(V):
                if not vis[j] and graph[U][j] != 0 and val[j] > dist + graph[U][j]:
                    val[j] = dist+graph[U][j]
                    heappush(pq, (j, val[j]))
                    parent[j] = U
        vis[U] = True

    # Print the val
    print(f"{val= }")
    print(f"{parent= }")


graph = [
    [0, 1, 4, 0, 0, 0],
    [1, 0, 4, 2, 7, 0],
    [4, 4, 0, 3, 5, 0],
    [0, 2, 3, 0, 4, 6],
    [0, 7, 5, 4, 0, 7],
    [0, 0, 0, 6, 7, 0]
]

djisktra(graph, 0)
