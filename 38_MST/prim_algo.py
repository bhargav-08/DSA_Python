
import sys


class Graph:
    def __init__(self,vertexNum,nodes,edges) -> None:
        self.edges = edges
        self.nodes = nodes
        self.vertexNum = vertexNum
        self.mst = []

    def print_solution(self):
        for s,d,w in self.mst:
            print(f"{s} -> {d} : {w}")

    def primsAlgo(self):
        visited = [0]*self.vertexNum
        edgenum = 0
        visited[0] =True

        while edgenum < self.vertexNum-1:
            min = sys.maxsize
            for i in range(self.vertexNum):
                if visited[i]:
                    for j in range(self.vertexNum):
                        if ((not visited[j]) and self.edges[i][j]):
                            if min > self.edges[i][j]:
                                min = self.edges[i][j]
                                s = i
                                d = j
            self.mst.append([self.nodes[s],self.nodes[d],self.edges[s][d]])
            visited[d]=True
            edgenum+=1

        self.print_solution()

nodes = ['A','B','C','D','E']
edges = [[0, 10, 20, 0, 0],
		[10, 0, 30, 5, 0],
		[20, 30, 0, 15, 6],
		[0, 5, 15, 0, 8],
		[0, 0, 6, 8, 0]]

g = Graph(5,nodes,edges)
g.primsAlgo()

# This is demo 