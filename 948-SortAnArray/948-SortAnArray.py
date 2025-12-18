# Last updated: 18/12/2025, 20:17:31
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr1 , arr2):
            aux  = []
            i, j = 0,0
            while i< len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j] :
                    aux.append(arr1[i])
                    i +=1
                else:
                    aux.append(arr2[j])
                    j +=1
            while i <len(arr1):
                aux.append(arr1[i])
                i +=1
            while j< len(arr2):
                aux.append(arr2[j])
                j +=1
 

            return aux
        def mergesort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) //2

            left = mergesort(arr[:mid])
            right = mergesort(arr[mid:])

            return merge(left, right)
        return mergesort(nums)
        
