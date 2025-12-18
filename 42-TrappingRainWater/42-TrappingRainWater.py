# Last updated: 18/12/2025, 20:21:07
class Solution: #comments by gpt
    def trap(self, height: List[int]) -> int:


        # two pointer


        n = len(height)
        left, right = 0, n - 1
        maxL, maxR = 0, 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= maxL:
                    maxL = height[left]
                else:
                    water += maxL - height[left]
                left += 1
            else:
                if height[right] >= maxR:
                    maxR = height[right]
                else:
                    water += maxR - height[right]
                right -= 1
        if 1==1:
            return water

        # Handle edge case where height list is empty
        if not height:
            return 0
        
        n = len(height)
        # Arrays to store the maximum height to the left and right of each bar
        left_max = [0] * n
        right_max = [0] * n
        water_trapped = 0
        
        # Initialize the first element of left_max with the height of the first bar
        left_max[0] = height[0]
        # Initialize the last element of right_max with the height of the last bar
        right_max[n-1] = height[n-1]
        
        # Compute the maximum height to the left of each bar
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])
        
        # Compute the maximum height to the right of each bar
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
        
        # Calculate the total amount of water trapped
        for i in range(n):
            # The water trapped at each bar is the minimum of the max heights on both sides minus the height of the bar
            water_trapped += min(left_max[i], right_max[i]) - height[i]
        
        return water_trapped


        
