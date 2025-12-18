# Last updated: 18/12/2025, 20:17:20
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
#Optimal substructure:
# If we know the longest arithmetic subsequence ending at index j with difference d,
# we can extend it to index i if nums[i] - nums[j] == d.

# Overlapping subproblems:
# The same difference d between pairs can occur multiple times with different subsequences.
                # dp[i][diff]. represent the longeest subsequence ending with the num[i] with difference diff such that diff = nums[i] - nums[j]
        dp  = [dict() for _ in range(len(nums))]
        ans = 0
        n = len(nums)
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] = dp[j].get(diff, 1) + 1
                ans = max(ans, dp[i][diff])
        return ans
