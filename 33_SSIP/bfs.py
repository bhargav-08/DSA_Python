
class Graph:
    def __init__(self,graph) -> None:
        self.graph = graph

    def bfs(self,start,end):
            q = []
            q.append([start])

            while q:
                path = q.pop(0)
                node = path[-1]

                if node==end:
                    return path
                for adjacent in self.graph[node]:
                    new_path = list(path)
                    new_path.append(adjacent)
                    q.append(new_path)


customdict = {
    "a":["b","c"],
    "b":["d","g"],
    "c":["d","e"],
    "d":["f"],
    "e":["f"],
    "g":["f"],
}
g = Graph(customdict)
print(g.bfs("a","f"))
