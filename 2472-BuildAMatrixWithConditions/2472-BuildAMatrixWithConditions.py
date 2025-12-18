# Last updated: 18/12/2025, 20:16:48
class Solution:
	def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
		rowadj = defaultdict(list)
		coladj = defaultdict(list)
		rowIndeg = [0] * (k + 1)
		colIndeg = [0] * (k+1)
		for con in rowConditions:
			rowadj[con[0]].append(con[1])
			rowIndeg[con[1]] +=1
		
		for con in colConditions:
			coladj[con[0]].append(con[1])
			colIndeg[con[1]] +=1
		
		#find topsort
		#lets define toposort
		def toposort(adj, indeg):
			order = []
			q = deque([node for node in range(1, k+1) if indeg[node] == 0 ])		
			while q:
				node = q.popleft()
				order .append(node)
				for friend in adj[node]:
					indeg[friend] -=1
					if indeg[friend] == 0:
						q.append(friend)
			

			if len(order) == k:
				return order
			return []
		rowOrder = toposort(rowadj, rowIndeg)
		colOrder = toposort(coladj, colIndeg)
		
		if len(rowOrder) == 0  or len(colOrder) == 0:
			return []
		arr = [[0 ] * k for _ in range(k)]
		rowpos = {num:i for i, num in enumerate(rowOrder)}
		colpos = {num: i for i, num in enumerate(colOrder)}
		for i in range(1, k+1):
			arr[rowpos[i]][colpos[i]] = i
		return arr