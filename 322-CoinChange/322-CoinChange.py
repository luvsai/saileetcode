# Last updated: 18/12/2025, 20:18:50
class Solution:
#dp[i] = fewest no of coins to make the amount i
# dp[i] = min(dp[i], min([dp[i-c] for c in coins]) + 1)

    coins = []
    memory = {}
    def mincoins(self,i, t):
        if ((i,t) in self.memory) :
            return self.memory[(i,t)]
        #base
        if i == 0:
            if t % self.coins[0] == 0:
                self.memory[(i,t)] = t // self.coins[0]
                return self.memory[(i,t)]
            else:
                self.memory[(i,t)] = float('inf')
                return self.memory[(i,t)]
        #npick
        npc = 0 + self.mincoins(i -1, t)

        #pick
        pc = float('inf')
        if t >= self.coins[i] :
            pc = 1 + self.mincoins(i, t-self.coins[i])
        self.memory[(i,t)] = min(pc,npc)
        return self.memory[(i,t)]

        #return minimum of them

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = coins
        n = len(coins)
        dp = [float('inf')] * (amount + 1)
        #dp[i] : states the min no of coins need to make up the amount i
        dp[0] = 0 # to make 0 removed we would need 0 coins

        for i in range(1, amount+1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1+ dp[i - c]) # 1 coin + rest of amount min
        return dp[amount] if dp[amount] != float('inf') else -1


            # self.memory = {}
            #val  = self.mincoins(n-1, amount) # recurssion with memoisation
            # if val == float('inf') :
            #     return -1
            # return val
        # T  = amount
        # dp = [[float('inf') for _ in range(T + 1)] for _ in range(n)]
        # for t in range(T+1):
        #     if t % coins[0] == 0:
        #         dp[0][t] = t // coins[0]
        #     else:
        #         dp[0][t] = float('inf')
        # for i in range (1,n):
        #     for t in range (0, T+ 1 ):
        #         #not pick 
        #         npc = dp[i-1][t]
        #         #pick
        #         pc = float('inf')

        #         if t >= coins[i]:
        #             pc = 1 + dp[i][t-coins[i]]
        #         dp[i][t] =  min(npc, pc)
        # val = dp[-1][-1]
        # if val == float('inf') :
        #     return -1
        # return val
 


        
        

        

        