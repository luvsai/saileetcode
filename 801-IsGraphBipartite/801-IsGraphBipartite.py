# Last updated: 18/12/2025, 20:17:50
from queue import Queue
from collections import deque
class Solution:
    def isbranchBP(self, start, graph, colors):
        colors[start] = 0
        q = deque([])
        q.append([start,0])

        while q:
            entry = q.popleft()
            node = entry[0]
            color = entry[1]
            ncolor = abs(1-color)
            for neighbor in graph[node]:
                if colors[neighbor] == -1:
                    colors[neighbor] = ncolor
                    q.append([neighbor, ncolor])
                else:
                    if colors[neighbor] == color:
                        return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
            # a graph is bipartite if all the nodes are colored with 2 different 
        #colors where no adjacent node colors are the same.
        V = len(graph)
        colors = [-1] * V
        start = 0
        while start < V:
            if colors[start] == -1 :
                if not self.isbranchBP(start, graph,colors):
                    return False
            start +=1
        # print(colors)
        return True