# Last updated: 18/12/2025, 20:17:21
# To solve this problem, you can use a Breadth-First Search (BFS) approach. Here's a step-by-step guide on how to approach the problem:

# 1. **Initialize**: Start by creating a queue to keep track of the rotten oranges' positions. Also, count the number of fresh oranges. You'll need this to determine when you've finished processing all the fresh oranges.

# 2. **Find Rotten Oranges**: Iterate through the grid and for each rotten orange (cell with value 2), add its position to the queue. Also, keep track of the number of fresh oranges you encounter.

# 3. **BFS Algorithm**: Perform the BFS from each rotten orange simultaneously. Here's how you can do it:
#	- While the queue is not empty, process oranges in the queue. This will represent one minute passing.
#	- For each rotten orange in the queue, check its 4-directional neighbors (up, down, left, right). If a neighbor is a fresh orange (cell with value 1), it becomes rotten.
#	- Change the value of the fresh orange to 2 and add its position to the queue for the next minute's processing.
#	- Decrease the count of fresh oranges by one each time a fresh orange becomes rotten.
#	- After processing all rotten oranges for the current minute, increment a minute counter.

# 4. **Check Completion**: After the BFS is complete, check if there are any fresh oranges left. If there are, it means that those oranges cannot be reached by the rotten ones, and you should return -1. Otherwise, return the minute counter, which represents the minimum number of minutes that must elapse until no cell has a fresh orange.

# 5. **Edge Cases**: Don't forget to handle edge cases, such as:
#	- The grid is empty (return 0).
#	- There are no fresh oranges at the start (return 0).
#	- There are no rotten oranges at the start (return -1).

# Remember, the BFS approach works well here because it naturally simulates the process of rot spreading from rotten oranges to adjacent fresh ones over time. Each level of the BFS represents one minute of time passing.
from collections import deque
class Solution:

	def orangesRotting(self, grid : List[List[int]]) -> int:
		rottenQ = deque()
		nofresh = 0
		m = len(grid)
		n = len(grid[0])
		mins = 0
		for i in range(m):
			for j in range(n):
				if grid[i][j] == 2:
					rottenQ.append((i,j))
				if grid[i][j] == 1:
					nofresh +=1	
			
		if nofresh == 0:
			return 0
		if len(rottenQ) == 0:
			return -1
		# print(rottenQ)
		while rottenQ:
			for _ in range(len(rottenQ)):
				y = rottenQ.popleft()
					# print(rottenQ)
				i,j = y
				directions = [(i , j + 1), (i+1 ,j), (i-1,j), (i,j-1)	]
				for dir in directions:
					ni, nj = dir
					# print(dir)
					if 0 <= ni < m and 0<= nj < n and grid[ni][nj] == 1 :
						# print("usdfsdf")
						grid[ni][nj] = 2
						rottenQ.append((ni,nj))
						nofresh -= 1
			if rottenQ:
				mins +=1

		# print(mins)
		if nofresh > 0 :
			return -1
		return mins