"""
City With the Smallest Number of Neighbors at a Threshold Distance
"""


def findCity(n: int, m: int, edges, distanceThreshold: int) -> int:
    cost = [[float('inf') if i != j else 0 for j in range(n)]
            for i in range(n)]

    # Create graph
    for u, v, wei in edges:
        cost[u][v] = wei
        cost[v][u] = wei

    for k in range(n):
        for i in range(n):
            for j in range(n):
                cost[i][j] = min(
                    cost[i][j],
                    cost[i][k] + cost[k][j]
                )
    cityCount = float("inf")
    city = -1

    for i in range(n):
        cityReachable = 0
        for j in range(n):

            if cost[i][j] <= distanceThreshold:
                cityReachable += 1

        if cityCount >= cityReachable:
            city = i
            cityCount = cityReachable

    return city


edges = [
    [0, 1, 2],
    [0, 4, 8],
    [1, 2, 3],
    [1, 4, 2],
    [2, 3, 1],
    [3, 4, 1],
]
print(findCity(5, 6, edges, 2))
