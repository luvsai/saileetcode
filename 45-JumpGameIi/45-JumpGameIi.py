# Last updated: 18/12/2025, 20:21:04
class Solution:
    def jump(self, nums: List[int]) -> int:
        # n = len(nums)
        # current_end = 0
        # farthest = 0
        # jumps = 0
        # for i in range(n-1):
        #     farthest = max(farthest, i + nums[i])
        #     if i == current_end:
        #         jumps += 1
        #         current_end = farthest
        # return jumps
        # n = len(nums)
        # currentdst = 0
        # swaps = 0

        # for i in range(n-1):
        #     if currentdst >= n-1:
        #         break
        #     if currentdst < i + nums[i] :
        #         swaps+=1
        #         currentdst = i + nums[i]
        # return swaps

        n = len(nums)

        best_power_bank_range = 0
        current_dst = 0
        swaps = 0
        for i in range(n-1):
            new_power_bank_range = i + nums[i]

            best_power_bank_range = max(best_power_bank_range , new_power_bank_range)

            # when i am at the destination powerbank station:
            # i think if i swap here or previous best power bank and since i reacorded the best_power_bank_range i would go and swap there and would continue my journey with new dest range.
            if current_dst == i:
                swaps +=1
                current_dst = best_power_bank_range
        return swaps



            

