# Last updated: 18/12/2025, 20:19:59
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n = rowIndex + 1
        final = [[1]]
        if n == 1:
            return final[-1]
        for i in range(1,n):
            temp = [1]* (i + 1)
            if i>1:
                for p in range(1,i):
                    temp[p] = final[-1][p-1] + final[-1][p]
            final.append(temp)
        
        return final[-1]