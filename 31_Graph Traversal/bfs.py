
class Graph:
    def __init__(self,gdict=None) -> None:
        if gdict is None:
            self.gdict = {}
        self.gdict = gdict

    def add(self,v1,v2):
        self.gdict[v1].append(v2)


    def bfs(self,initial):
        queue = [initial]
        visited = [initial]
        while queue:
            deVertex = queue.pop(0)
            print(deVertex,end=" ")

            for adjacent_nodes in self.gdict[deVertex]:
                if adjacent_nodes not in visited:
                    queue.append(adjacent_nodes)
                    visited.append(adjacent_nodes)

        print(visited)

    def dfs(self,initial):
        stack = [initial]
        visited = [initial]
        while stack:
            deVertex = stack.pop()
            print(deVertex,end=" ")

            for adjacent_nodes in self.gdict[deVertex]:
                if adjacent_nodes not in visited:
                    stack.append(adjacent_nodes)
                    visited.append(adjacent_nodes)
        print(visited)
    """
    def bfs(self,initial):
            queue = [initial]
            visited = []
            while queue:
                deVertex = queue.pop(0)
                if deVertex not in visited:
                    print(deVertex,end=" ")
                    visited.append(deVertex)
                    queue.extend(self.gdict[deVertex])
"""

dict = {
    "A":["B","C"],
    "B":["A","E","D"],
    "C":["A","E"],
    "D":["B","E","F"],
    "E":["C","D","B"],
    "F":["D","E"]
}

g = Graph(dict)
g.bfs("A")
print()
# g.dfs("A")