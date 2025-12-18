# Last updated: 18/12/2025, 20:16:43
from collections import Counter
MOD = 10**9 + 7
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        ans = 0
        leftwindow = Counter()
        rightwindow = Counter(nums)
        
        for el in nums:
            rightwindow[el] -=1
            if rightwindow[el] == 0:
                del rightwindow[el]
            
            need = 2 * el
            ans = ( ans + leftwindow.get(need, 0) * rightwindow.get(need, 0)) % MOD
            
            # push the el into the left window
            leftwindow[el] +=1


        return ans

        
