# Last updated: 18/12/2025, 20:18:09
class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

    def findParent(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.findParent(self.parent[node])  # path compression
        return self.parent[node]

    def unionByRank(self, u, v):
        pu = self.findParent(u)
        pv = self.findParent(v)

        if pu == pv:
            return False  # same parent → cycle formed

        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pv] < self.rank[pu]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
        return True
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        ds = DisjointSet(n)

        for u, v in edges:
            if not ds.unionByRank(u, v):
                return [u, v]  # This edge creates a cycle