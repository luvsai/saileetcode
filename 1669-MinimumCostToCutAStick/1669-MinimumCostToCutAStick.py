# Last updated: 18/12/2025, 20:17:04
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:

        #tabulation bottom up:
        cuts = [0] + sorted(cuts) + [n]

        m = len(cuts)
        dp = [[0] * m for _ in range(m)]

        #lenght is the gap between i and j ( we need at least  one interior index to cut)
        for length in range(2, m):
            for i in range(0, m -length): # i starts from 0 since boundareis 
                j = i + length
                best = float('inf')
                for k in range(i+ 1, j):
                    cost = dp[i][k] + dp[k][j] + (cuts[j] - cuts[i])
                    best = min(best, cost)
                dp[i][j] = 0 if best == float('inf') else best




        return dp[0][m-1]


    



        # pad and sort
        cuts = [0] + sorted(cuts) + [n]
        dp = {}
        m = len(cuts)

        def solve (i, j): # min cost to make the cuts between the boundaries cuts[i] , cuts[j]
            if (i, j) in dp:
                return dp[(i,j)]
            #base case
            if j == i+1:
                # we dont need to cut this stick #since no valid cuts present between the indices
                return 0# cost is 0
            best = float('inf')
            for k in range(i + 1, j):
                cost = solve(i, k) + solve(k,j ) + (cuts[j] - cuts[i])
                best = min(cost, best)
            dp[(i,j)] = best
            return best
        return solve(0,m-1) # cost to cut the stick between boundaries of cuts[0] with is left edge and cust[m-1] which i right edge of value n

