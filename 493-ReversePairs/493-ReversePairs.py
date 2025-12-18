# Last updated: 18/12/2025, 20:18:26
class Solution:
    rpcount = 0
    def merge(self,arr1, arr2):
        if not arr1 or not arr2:
            return 
        aux = []
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

    def countpairs(self,arr1, arr2):
        if not arr1 or not arr2:
            return 
            
        i , j = 0,0

        while i< len(arr1) and j < len(arr2):
            if arr1[i] > 2 * arr2[j]:
                self.rpcount += (len(arr1) - i)
                j +=1
            else:
                i +=1
        

    def reversePairs(self, nums: List[int]) -> int:

        
        
        def mergesort(arr) :
            if len(arr) <=1:
                return arr
            mid = len(arr)//2

            left = mergesort(arr[:mid])
            right = mergesort(arr[mid:])

            self.countpairs(left ,right)
            return self.merge(left, right)

        mergesort(nums)
        return self.rpcount

        
        





