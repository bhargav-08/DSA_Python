""" 743. Network Delay Time
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
"""
from heapq import *


def networkDelayTime(times, n: int, k: int) -> int:
    adj = {i: [] for i in range(1, n+1)}
    for u, v, w in times:
        adj[u].append((v, w))

    dist = [float("inf")]*(n+1)
    dist[n] = 0
    pq = []
    heappush(pq, (0, k))

    while pq:
        d, U = heappop(pq)

        for nei, w in adj[U]:
            if dist[nei] > d + w:
                dist[nei] = d + w
                heappush(pq, (dist[nei], nei))

    print(dist)

    return 0


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
print(networkDelayTime(times, n, k))

["Graph","shortestPath","addEdge","shortestPath","addEdge","addEdge","addEdge","addEdge","addEdge","addEdge","shortestPath","shortestPath","addEdge","shortestPath","addEdge","shortestPath","addEdge","addEdge","addEdge"]
[[13,[[7,2,131570],[9,4,622890],[9,1,812365],[1,3,399349],[10,2,407736],[6,7,880509],[1,4,289656],[8,0,802664],[6,4,826732],[10,3,567982],[5,6,434340],[4,7,833968],[12,1,578047],[8,5,739814],[10,9,648073],[1,6,679167],[3,6,933017],[0,10,399226],[1,11,915959],[0,12,393037],[11,5,811057],[6,2,100832],[5,1,731872],[3,8,741455],[2,9,835397],[7,0,516610],[11,8,680504],[3,11,455056],[1,0,252721]]]
 
 ,[9,3],[[11,1,873094]],[3,10],[[0,9,601498]],
 [[12,0,824080]],[[12,4,459292]],[[6,9,7876]],[[11,7,5479]],[[11,12,802]],[2,9],[2,6],[[0,11,441770]],[3,7],[[11,0,393443]],[4,2],[[10,5,338]],[[6,1,305]],[[5,0,154]]]