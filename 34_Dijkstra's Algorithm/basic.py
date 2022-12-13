from collections import defaultdict


class Graph:
    def __init__(self) -> None:
        self.nodes = set()
        self.distance = {}
        self.edges = defaultdict(list)

    def addNode(self,node):
        self.nodes.add(node)

    def addEdge(self,fromNode,toNode,distance):
        self.edges[fromNode].append(toNode)
        self.distance[(fromNode,toNode)] = distance

def dijkstra(graph,inital):
    visited = {inital:0}
    nodes = set(graph.nodes)
    path = defaultdict(list)

    while nodes:
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] <visited[minNode]:
                    minNode = node
        if minNode is None:
            break

        nodes.remove(minNode)
        weight = visited[minNode]

        for edge in graph.edges[minNode]:
            currentWeight = weight + graph.distance[(minNode,edge)]
            if edge not in visited or visited[edge] > currentWeight:
                visited[edge] = currentWeight
                path[edge].append(minNode)

    return visited,path

customGraph = Graph()
customGraph.addNode("A")
customGraph.addNode("B")
customGraph.addNode("C")
customGraph.addNode("D")
customGraph.addNode("E")
customGraph.addNode("F")
customGraph.addNode("G")
customGraph.addEdge("A", "B", 2)
customGraph.addEdge("A", "C", 5)
customGraph.addEdge("B", "C", 6)
customGraph.addEdge("B", "D", 1)
customGraph.addEdge("B", "E", 3)
customGraph.addEdge("C", "F", 8)
customGraph.addEdge("D", "E", 4)
customGraph.addEdge("E", "G", 9)
customGraph.addEdge("F", "G", 7)

print(dijkstra(customGraph, "A"))

