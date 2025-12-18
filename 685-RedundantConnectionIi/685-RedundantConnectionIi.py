# Last updated: 18/12/2025, 20:18:08
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = {}
        candidate1 = None
        candidate2 = None

        # step 1 is to find the candidate 1 and 2 node which has two parents
        for u, v in edges:
            if v in parent:
                candidate1 = [parent[v],v]
                candidate2 = [u, v]
            parent[v] = u
        
        uf = {i:i for i in range(1, n+1)}
        
        # Helper DSU
        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        def union(x,y):
            px, py = find(x) , find(y)
            if px == py:
                return False # cycle formed
            uf[py] = px
            return True
        
        # step 2 ignore as if candite 2 doesnot exists and try to find the cycle , 
        for u, v in edges:
            if [u, v] == candidate2:
                continue
            if not union(u,v): # cycle formed by joining u, v
                if candidate1:
                    return candidate1
                return [u,v]
        return candidate2

