# Last updated: 18/12/2025, 20:17:10
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        minsrows = set()
        maxcols = set()
        for i in range(m):
            rowmin = matrix[i][0]
            for j in range(n):
                if matrix[i][j] < rowmin:
                    rowmin = matrix[i][j]
            minsrows.add(rowmin)
        for i in range(n):
            colmax= matrix[0][i]
            for j in range(m):
                if matrix[j][i] > colmax:
                    colmax = matrix[j][i]
            maxcols.add(colmax)
        # print(minsrows, maxcols)
        finalset = []
        for minel in minsrows:
            if minel in maxcols:
                finalset.append(minel)
        return finalset
        