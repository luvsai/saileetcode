# Last updated: 18/12/2025, 20:19:56
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        hold = -prices[0]
        not_hold = 0

        for i in range(1,len(prices)):
            new_hold = max(hold, not_hold -prices[i])
            new_not_hold = max(hold + prices[i], not_hold)
        
            hold, not_hold = new_hold, new_not_hold
        
        return not_hold