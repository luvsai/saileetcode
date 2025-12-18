# Last updated: 18/12/2025, 20:18:53
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        hold = [0] * n
        sold = [0] * n
        rest = [0] * n

        #base cases
        hold[0] = -prices[0]
        sold[0] = 0
        rest[0] = 0

        for i in range(1, n):
            
            # HOld the stock : you either bought today and was in rest yestterday or you were holding from yesterday
            hold[i] = max( rest[i-1] - prices[i] , hold[i-1])

            # sold the stock: you sold the stock that you are holding from yesterday
            sold[i] = hold[i-1] + prices[i]

            # rest : you either sold yesterday and resting today. or you were resting
            rest[i] = max(rest[i-1], sold[i-1])

        # day n-1 you either sell the holding stock or you wer resting
        return max(sold[-1], rest[-1])
