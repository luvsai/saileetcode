# Last updated: 18/12/2025, 20:19:30
from functools import lru_cache

class Solution:
    @lru_cache
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n-1
            count +=1
        return count

        # while n>0:
        #     count += n & 1
        #     n >>= 1
        # return count