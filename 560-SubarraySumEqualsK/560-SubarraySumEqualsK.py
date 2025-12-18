# Last updated: 18/12/2025, 20:18:17
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_map = {0:1}# for current prefix_sum which is 0 since we start with 0

        for num in nums:
            prefix_sum += num
            if prefix_sum - k in prefix_map:
                count += prefix_map[prefix_sum - k]
            
            #Store / update the prefix_sum
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
        return count