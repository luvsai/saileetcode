# Last updated: 18/12/2025, 20:19:31
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        

# k = 0 means no transaction 
# k = 1 means one transaction
# k = 2 means two transaction

        n = len(prices)
        if n == 0:
            return 0
        
        NF = float('-inf')
        maxtransactions = k + 1
        # dp[i][t][h] in [0..n-1] , t in[0..2] , h in {0,1}
        dp = [[[NF for _ in range(2)]  for _ in range(maxtransactions)   ] for _ in range(n)]

        #base for day 0
        dp[0][0][0] = 0 # not holding , no transaction commited profit 0
        dp[0][0][1] = -prices[0] # bought stock

        # rest of the transactions state whethere holding or not holding are NF invalid
        for i in range(1,maxtransactions):
            dp[0][i][0] = NF
            dp[0][i][1] = NF
        

        # transitions
        for i in range(1, n):
            for t in range(maxtransactions):
                #Not holding h = 0
                ## Do nothing
                best_not_hold = dp[i-1][t][0]    

                # sell today
                if t>=1 and dp[i-1][t-1][1] != NF:
                    best_not_hold = max(best_not_hold, dp[i-1][t-1][1] + prices[i])
                dp[i][t][0] = best_not_hold

                #holding on day 1 => h =1
                # do nothing
                best_hold = dp[i-1][t][1]

                #buy today
                if dp[i-1][t][0] != NF:
                    best_hold = max(best_hold, dp[i-1][t][0] - prices[i])
                dp[i][t][1] = best_hold
        maxprofit = max([dp[n-1][i][0] for i in range(maxtransactions)  ] )
        return maxprofit