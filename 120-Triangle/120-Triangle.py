# Last updated: 18/12/2025, 20:19:58
class Solution:

    # if you see it its like a recursion tree leaf nodes are depth of the tree. now as we move from leaf to top at each node we verify for node [i][j] [i+1][j] and [i+1][j+1] are children and what we return is current node + min of left and right child values.
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len( triangle ) == 1:
            return triangle[0][0]
        n = len(triangle)
        for i in range(n-2,-1,-1):
            for j in range(len(triangle[i])):
                triangle [i][j] += min(triangle[i+1][j],triangle[i+1][j+1])
        return triangle[0][0]

        