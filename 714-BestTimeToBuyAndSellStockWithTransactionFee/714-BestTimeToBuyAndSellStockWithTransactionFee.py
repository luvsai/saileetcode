# Last updated: 22/12/2025, 19:27:13
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        nothold = 0
        hold = 0

        # base conditiaon on day 1
        nothold = 0 
        hold = -prices[0] # we add transaction fee only when we sell the stock

        for price in prices[1:]:
            new_nothold = max(nothold, hold + price -fee)
            new_hold = max(hold, nothold - price)

            nothold = new_nothold
            hold = new_hold
        return nothold