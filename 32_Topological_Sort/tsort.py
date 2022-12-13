
from collections import defaultdict

class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def addEdge(self,vertex,edge):
        self.graph[vertex].append(edge)

    def topologicalUtility(self,v,visited,stack):
        visited.append(v)

        for i in self.graph[v]:
            if i not in visited:
                self.topologicalUtility(i,visited,stack)
        stack.insert(0,v)

    def topologicalSort(self):
        visited = []
        stack = []

        for i in list(self.graph):
            if i not in visited:
                self.topologicalUtility(i,visited,stack)
        print(stack)


# g = Graph()
# g.add("A","C")
# g.add("B","C")
# g.add("B","D")
# g.add("C","E")
# g.add("E","H")
# g.add("E","F")
# g.add("D","F")
# g.add("F","G")

g = Graph()
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(2,4)
g.addEdge(3,5)
g.addEdge(5,4)
g.addEdge(5,2)
g.addEdge(4,6)
g.addEdge(5,6)

# print(g.graph)
g.topologicalSort()
