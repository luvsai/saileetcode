# Last updated: 18/12/2025, 20:20:01
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows
        final = [[1]]
        if n == 1:
            return final
        for i in range(1,n):
            temp = [1]* (i + 1)
            if i>1:
                for p in range(1,i):
                    temp[p] = final[-1][p-1] + final[-1][p]
            final.append(temp)
        
        return final