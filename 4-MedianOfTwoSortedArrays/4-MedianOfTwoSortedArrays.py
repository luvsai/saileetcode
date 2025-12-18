# Last updated: 18/12/2025, 20:21:30
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1; B = nums2
        if len(A) > len(B):
            A, B = B, A
            # A should be the smallest array
        m, n = len(A) , len(B)
        total = m + n
        half = (total + 1) //2
        low , high = 0, m

        while low <= high:
            i = (low + high)//2 #take i elements from A
            j = half -i
            Aleft = A[i-1] if i> 0 else float('-inf')
            Aright = A[i] if i < m else float('inf')
            Bleft = B[j-1] if j > 0 else float('-inf')
            Bright = B[j] if j< n else float('inf')

            if Aleft <=Bright and Bleft <= Aright:
                # correct partition
                if total % 2 == 1:
                    return max(Aleft, Bleft)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) /2

            elif Aleft >Bright:
                high = i-1
            else:
                low = i + 1

    