
class Disjoint:
    def __init__(self,vertices) -> None:
        self.vertices = vertices
        self.parent = {}
        for v in self.vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(self.vertices,0)

    def findP(self,item):
        if self.parent[item]==item:
            return item
        else:
            return self.findP(self.parent[item])

    def union(self,x,y):
        xroot= self.findP(x)
        yroot= self.findP(y)
        if self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        elif self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot]+=1

nodes = ['A', 'B', 'C', 'D', 'E']
ds = Disjoint(nodes)

ds.union('A','C')
ds.union('B','E')
ds.union('B','C')
print(ds.rank)
print(ds.findP('B'))
print(ds.parent)