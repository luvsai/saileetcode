# Last updated: 18/12/2025, 20:19:57
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mbp = float(inf)
        maxprofit = 0
        for price in prices:
            if price < mbp:
                mbp = price
            else:
                currprofit = price - mbp
                maxprofit = max(currprofit , maxprofit)
        return maxprofit

        