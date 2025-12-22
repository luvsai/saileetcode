# Last updated: 22/12/2025, 19:27:17
from typing import List

class FenwickTree:
    def __init__(self, size):
        self.tree = [(0, 0)] * (size + 1)

    def merge(self, a, b):
        # a, b are (length, count)
        if a[0] > b[0]:
            return a
        if b[0] > a[0]:
            return b
        return (a[0], a[1] + b[1])

    def query(self, i):
        # returns (max_length, count) in range [1..i]
        res = (0, 0)
        while i > 0:
            res = self.merge(res, self.tree[i])
            i -= i & -i
        return res

    def update(self, i, val):
        # val is (length, count)
        while i < len(self.tree):
            self.tree[i] = self.merge(self.tree[i], val)
            i += i & -i


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Coordinate compression
        sorted_unique = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(sorted_unique)}

        fenwick = FenwickTree(len(sorted_unique))

        for x in nums:
            r = rank[x]

            # Query all values < x
            best_len, ways = fenwick.query(r - 1)

            if best_len == 0:
                cur = (1, 1)
            else:
                cur = (best_len + 1, ways)

            fenwick.update(r, cur)

        return fenwick.query(len(sorted_unique))[1]

# class Solution:
#     def findNumberOfLIS(self, nums: List[int]) -> int:
        




#         n = len(nums)
#         dp = [1] * n # length of the longest increasing sequence ending at index i
#         count = [1] * n # no of the longest incresing sequence ending at index i

#         # answer would using max(dp) find the longest and sum up the count of teh such sequences.
#         # dp represents longest sequence ending at i.
#         # we need global longest sequence which would be max(dp array)
#         longestseq = 1
#         for i in range(1, n):
#             for j in range(i):
#                 if nums[j] < nums[i]:

#                     if dp[j] + 1> dp[i]:
#                         dp[i] = dp[j] + 1
#                         count[i] = count[j]
#                     elif dp[j] + 1 == dp[i]:
#                         count[i] += count[j]

#                     #dp[i] = max(dp[i], dp[j] + 1) expanded above

#                 longestseq  = max(longestseq, dp[i])
#         ans = 0
#         for i in range(n):
#             if dp[i] == longestseq:
#                 ans += count[i]
        
#         return ans
        