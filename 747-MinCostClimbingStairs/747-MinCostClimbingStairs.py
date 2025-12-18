# Last updated: 18/12/2025, 20:17:58
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        twostepdown = cost[0]
        onestepdown =  cost[1]
        n = len(cost)
        nstep = 0
        for i in range(2, n):
            nstep = cost[i] + min(onestepdown, twostepdown)
            twostepdown = onestepdown
            onestepdown = nstep
        return min(onestepdown , twostepdown)
        
        # follow the below.
        n = len(cost)
        dp= [0] * n
        #dp[i] => min cost to reach to the top of the floor via the step i
        dp[0] = 0 + cost[0]# via dp[0] it would be min cost to reach zero and than cost to leave zero
        dp[1] = 0 + cost[1] # since we can start from 1 to min cost to reach 1 is 0 and to leave index 1 would be the cost to leave the index.
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        # cost to reach the step n would be min(cost to reach previous step , cost to reach two steps down) 
        return min(dp[n-1], dp[n-2])

        