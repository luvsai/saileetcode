# Last updated: 08/01/2026, 19:55:08
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        # brute force is o(n2) find all subarrays and the peak and 

        # optimized find the peaks using at every i check if i-1 and i +1 element are peaks and peaks
        maxdiameter = 0
        i = 1
        n = len(arr)
        while i < n-1:
            if arr[i-1] < arr[i] > arr[i+1]:
                left = i -1
                right = i +1
                while left > 0 and arr[left] > arr[left -1]:
                    left -=1
                while right < n-1 and arr[right] > arr[right +1]:
                    right +=1
                
                maxdiameter = max(maxdiameter, right - left + 1)

                i = right # skip the processed mountain
            else:
                i +=1
        return maxdiameter