# Last updated: 18/12/2025, 20:17:47
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        #reverse the graph
        rev = [[] for _ in range(n)]
        outdegree = [0] * n

        for u in range(n):
            for v in graph[u]:
                rev[v] .append(u)
            outdegree[u] = len(graph[u])
        
        from collections import deque

        q = deque([i for i in range(n) if outdegree[i] == 0])
        safe = [False] * n
        while q:
            node = q.popleft()
            safe[node] = True

            for parent in rev[node]:
                outdegree[parent] -=1
                if outdegree[parent] == 0:
                    q.append(parent)
        return [i for i in range(n) if safe[i]]

        