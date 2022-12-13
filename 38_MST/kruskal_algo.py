
from disjoint import Disjoint


class Graph:
    def __init__(self, vertices) -> None:
        self.V = vertices
        self.graph = []
        self.nodes = []
        self.MST = []

    def addNode(self, node):
        self.nodes.append(node)

    def addEdge(self, s, d, w):
        self.graph.append([s, d, w])

    def print_solution(self, s, d, w):
        for s, d, w in self.MST:
            print(f"{s} -> {d} : {w}")

    def kruskalAlgo(self):
        i, e = 0, 0
        graph = sorted(self.graph, key=lambda item: item[2])
        ds = Disjoint(self.nodes)
        while e < self.V-1:
            s, d, w = graph[i]
            x = ds.findP(s)
            y = ds.findP(d)
            i += 1
            if x != y:
                ds.union(x, y)
                e += 1
                self.MST.append([s, d, w])
        self.print_solution(s, d, w)


g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.addEdge("A", "B", 5)
g.addEdge("A", "C", 13)
g.addEdge("A", "E", 15)
g.addEdge("B", "A", 5)
g.addEdge("B", "C", 10)
g.addEdge("B", "D", 8)
g.addEdge("C", "A", 13)
g.addEdge("C", "B", 10)
g.addEdge("C", "E", 20)
g.addEdge("C", "D", 6)
g.addEdge("D", "B", 8)
g.addEdge("D", "C", 6)
g.addEdge("E", "A", 15)
g.addEdge("E", "C", 20)

g.kruskalAlgo()
