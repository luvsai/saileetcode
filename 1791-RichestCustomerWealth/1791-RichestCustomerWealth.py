# Last updated: 18/12/2025, 20:16:59
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richcustomer = [-1, float('-inf')] #(index + 1, wealth)
        for i in range(len(accounts)):
            rsum = 0
            for j in range(len(accounts[0])):
                rsum += accounts[i][j]
            if rsum > richcustomer[1] :
                richcustomer[0] = i +1
                richcustomer[1] = rsum
        return richcustomer[1]



        