# Last updated: 18/12/2025, 20:18:56
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = []
        n = len(nums)
        def searchrighbound(arr, el ):
            left = 0; right = len(arr) 
            while left < right:
                mid = (left + right) //2
                if  arr[mid] < el:
                    left = mid + 1
                else:
                    right = mid 
            return left
        if n == 1:
            return 1
        arr.append(nums[0])
        for idx in range(1, n):
            if arr[-1] < nums[idx] :
                arr.append(nums[idx])
            else:
                rb =   searchrighbound(arr, nums[idx])
                arr[rb] = nums[idx]
        return len(arr)

            







        n = len(nums)
        dp = [1] * n



        # dp represents longest sequence ending at i.

        # we need global longest sequence which would be max(dp array)
        longestseq = 1
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    longestseq  = max(longestseq, dp[i])
        return longestseq
        