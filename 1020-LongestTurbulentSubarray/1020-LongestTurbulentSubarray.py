# Last updated: 22/12/2025, 19:26:49
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if not arr:
            return 0
        
        # up[i] → last movement went up <
        # down[i] -> last move went down >
        # A single element is trivially turbulent of length 1.
        up = down = 1
        res = 1

        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]: # this is perceived as arr[i -1] < arr[i] 
                up = down + 1 # up[i]
                down = 1
            elif arr[i] < arr[i-1]:
                
                down  = up + 1 #down[i]
                up = 1
            else: # both are same elements
                up = down = 1
            res = max(res, up , down) # since sub array just like kadane we need local maxima
        return res