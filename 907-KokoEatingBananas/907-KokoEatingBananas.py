# Last updated: 18/12/2025, 20:17:33
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canfinish(k, h, piles):
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile/k)
            return hrs <=h
        left , right = 1, max(piles)
        while left < right:
            mid = (left + right) //2
            if canfinish(mid,h,piles):
                right = mid 
            else:
                left = mid + 1
        return left