# Last updated: 18/12/2025, 20:20:33
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        low =0
        mid = 0
        high = n-1
        while mid < high and mid <= n-1:
            if nums[mid] == 0:
                temp = nums[low] 
                nums[low] = nums[mid]
                nums[mid] = temp
                low +=1
                mid +=1
            elif nums[mid] == 1:
                    mid += 1
            elif nums[mid] == 2:
                #swap high and mid and decrement high
                temp = nums[mid]
                nums[mid] = nums[high]
                nums[high] = temp
                high -=1
            else :
                pass
            print(nums)
        if mid <= n-1 and nums[mid] == 0:
            temp = nums[low] 
            nums[low] = nums[mid]
            nums[mid] = temp
            low +=1
            mid +=1
        return nums