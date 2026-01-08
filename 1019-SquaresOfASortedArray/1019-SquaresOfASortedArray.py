# Last updated: 08/01/2026, 19:54:57
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]* n

        left ,right = 0, n-1
        pos = n-1
        while left <=right:
            if abs(nums[left]) > abs(nums[right]):
                res[pos] = nums[left] * nums[left]
                left +=1
            else:
                res[pos] = nums[right] * nums[right]
                right -=1
            pos -=1
        return res

        

        