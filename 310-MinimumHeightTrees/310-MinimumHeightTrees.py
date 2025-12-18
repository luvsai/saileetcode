# Last updated: 18/12/2025, 20:18:52
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    
            #edge case 
        if n==1:
            return  [0]
        #Build adjacency 
        graph = defaultdict(set)
        for a, b in edges:
            graph[b].add(a)
            graph[a].add(b)
        
        # initialize the first layer of leaves
        leaves = [i for i in range(n) if len(graph[i]) == 1]
            
        remaining_nodes = n
        while remaining_nodes >2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves # moving inward
        return leaves