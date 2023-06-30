# Find whether it is possible to color all the node with atmost m color with no two adjacent node having same color
def graphColoring(graph, k, V):
    color = [-1]*V

    def isPossible(node, clr):
        for idx, nei in enumerate(graph[node]):
            if nei and color[idx] == clr :
                return False
        return True

    def solve(node):
        if node == V:
            return True

        for clr in range(k):
            if isPossible(node, clr):
                color[node] = clr
                return solve(node+1)

                # if solve(node+1):
                #     return True
                # color[node] = -1       

        return False

    return solve(0)
