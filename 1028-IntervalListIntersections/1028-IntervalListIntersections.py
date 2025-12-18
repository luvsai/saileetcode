# Last updated: 18/12/2025, 20:17:24
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j= 0
        res = []
        A= firstList
        B = secondList

        while i < len(A) and j < len(B):
            a_start, a_end = A[i]
            b_start, b_end = B[j]

            #Find overlap start and end
            start = max(a_start, b_start)
            end = min(a_end , b_end)

            if start<=end:
                res.append([start, end])
            if a_end < b_end:
                i+=1
            else:
                j +=1
        return res
