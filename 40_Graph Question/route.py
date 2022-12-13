from re import L


def validateRoute(s,e,graph):
    queue = [s]
    visited = [s]

    while queue:
        v = queue.pop(0)
        for i in graph[v]:
            if i not in visited:
                if i==e:
                    print("Path does exist!")
                    return True
                else:
                    visited.append(i)
                    queue.append(i)


    print("Route does not Exist!!")
    return 

graph = {
    'A':['C','D','B'],
    'B':['J'],
    'C':['G'],
    'D':[],
    'E':['A','F'],
    'F':['I'],
    'G':['H'],
    'H':[],
    'J':[],
    'I':[],
}

validateRoute('A','H',graph)