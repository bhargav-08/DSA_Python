class Graph:
    def __init__(self,gdict=None) -> None:
        if gdict is None:
            self.gdict = {}
        self.gdict = gdict

    def add(self,v1,v2):
        self.gdict[v1].append(v2)

dict = {
    "A":["B","C"],
    "B":["E","D"],
    "C":["A","E"],
    "D":["E","F"],
    "E":["C","D","B"],
    "F":["D","E"]
}
g = Graph(dict)
print(g.gdict)
g.add("E","A")
print(g.gdict)
