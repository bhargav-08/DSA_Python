
class Graph:
    def __init__(self,matrix) -> None:
        self.graph = matrix

    def print_solution(self,matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                print(matrix[i][j],end=" ")
            print()

    def floydalgo(self):
        vertix = len(self.graph)
        dist = self.graph

        for k in range(vertix):
            for i in range(vertix):
                for j in range(vertix):
                    dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])


        self.print_solution(dist)


INF = 99999
G = [[0, 8, INF,1],
    [INF, 0, 1,INF],
    [4, INF, 0,INF],
    [INF, 2, 9,0]
    ]

g = Graph(G)
g.floydalgo()