# Last updated: 18/12/2025, 20:18:37
class Solution:
    #Time	O(m × n)	Each cell added to each queue at most once (Pacific & Atlantic).
#Space	O(m × n)	For queues and visited sets.
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        rows, cols = len(heights), len(heights[0])
        
        pacific_queue = deque()
        atlantic_queue = deque()
        pacific_visited = set()
        atlantic_visited = set()

        # Step 1: Initialize border cells
        for c in range(cols):
            pacific_queue.append((0, c))
            pacific_visited.add((0, c))
            atlantic_queue.append((rows - 1, c))
            atlantic_visited.add((rows - 1, c))
        
        for r in range(rows):
            pacific_queue.append((r, 0))
            pacific_visited.add((r, 0))
            atlantic_queue.append((r, cols - 1))
            atlantic_visited.add((r, cols - 1))

        # Helper BFS function
        def bfs(queue, visited):
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows and
                        0 <= nc < cols and
                        (nr, nc) not in visited and
                        heights[nr][nc] >= heights[r][c]  # can flow "uphill"
                    ):
                        visited.add((nr, nc))
                        queue.append((nr, nc))
        
        # Step 2: BFS for both oceans
        bfs(pacific_queue, pacific_visited)
        bfs(atlantic_queue, atlantic_visited)

        # Step 3: Intersection
        result = list(pacific_visited & atlantic_visited)
        return result