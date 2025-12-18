# Last updated: 18/12/2025, 20:17:22
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # find the maximum window with or 0 or 1 or 2 and than return. 
        left = 0 
        right = 0
        maxlen = 0
        zerocount = 0
        while right < len(nums):
            if nums[right] == 0:
                zerocount +=1
            while zerocount >k :
                if nums[left] == 0:
                    zerocount -=1
                left +=1
            maxlen = max( maxlen, right -left +1 )
            right +=1

        
        return maxlen






#         💡 Intuition — Sliding Window (expand–shrink)

# We need the longest window that has at most k zeros.

# Expand right pointer r each step.

# Count how many zeros are inside the window.

# If zeros > k → shrink the window from left (l += 1) until zeros ≤ k.

# Track the max window size at every step.

# It’s the same pattern as “Longest substring with ≤ k bad chars.”