class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.size = [1 for _ in range(n + 1)]

    def findUPar(self, node):
        if self.parent[node] == node:
            return node

        res = self.findUPar(self.parent[node])
        self.parent[node] = res
        return res

    def unionBySize(self, u, v):
        pu = self.findUPar(u)
        pv = self.findUPar(v)

        if pu == pv:
            return
        elif self.size[pu] < self.size[pv]:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        else:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
