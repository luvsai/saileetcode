# Last updated: 18/12/2025, 20:19:38
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Initialize max_product, min_product, and global_max with the first element
        max_product = min_product = global_max = nums[0]
        
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            current = nums[i]
            
            # Since the current number could be negative, swap max and min when necessary
            if current < 0:
                max_product, min_product = min_product, max_product
            
            # Calculate the new max and min products
            max_product = max(current, max_product * current)
            min_product = min(current, min_product * current)
            
            # Update the global maximum product
            global_max = max(global_max, max_product)
        
        return global_max