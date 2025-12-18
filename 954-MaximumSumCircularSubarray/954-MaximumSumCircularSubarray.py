# Last updated: 18/12/2025, 20:17:30
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        ## circular arry pick not pick 
        # we need to exclude elements array so we willmake horse shoe. U kinda of first index and last index are connected right. we need to exclude consecutive min num sum so we get maximum num sum of remaininng elements
# if we negate the sign we can use kadane for maximum sum 
        sumOfNums = 0
        currsum = 0
        maxSum = nums[0]

        minSum = -1 * nums[0]
        mincurrSum = 0

        for num in nums :
            #to get the total sum
            sumOfNums += num
            
            # kadane algo
            currsum += num
            maxSum = max(currsum, maxSum)
            if currsum < 0:
                currsum = 0

            # inverted kadane algorigth
            num = num * -1

            mincurrSum += num
            minSum = max(minSum, mincurrSum)
            if mincurrSum < 0:
                mincurrSum = 0
        if maxSum < 0:
            return maxSum

        return max(maxSum ,sumOfNums + minSum)
        
        # kadane to find the m ## use kadane above its self
