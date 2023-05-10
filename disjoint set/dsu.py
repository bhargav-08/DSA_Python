dsup = [-1]*5


def find(vertex):
    while dsup[vertex] != -1:
        vertex = dsup[vertex]

    return vertex


def union(v1, v2):
    p1 = find(v1)
    p2 = find(v2)
    if p1 != p2:
        dsup[v2] = p1


union(1, 2)
union(1, 3)
union(3, 4)

print(find(4))
