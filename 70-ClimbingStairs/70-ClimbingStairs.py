# Last updated: 18/12/2025, 20:20:40
class Solution:
    def climbStairs(self, n: int) -> int:


#### blue print for any dynamic programming problem

# from the explanation:
# if n = 2 we have two ways implies we are starting from step 0. and we are reaching step n which is 2

##1 wrtie the problem statement in terms of index i
# we need to find the no of distinct ways to reach step n dp[n] if we start from step 0
# dp[i] represents no of distinct ways to reach step i starting from step 0

##2 write the base conditions and recurring condtions
# dp[0] since we start from step 0 we need to write how many distinct ways to reach step 0 that is 1 way.

# to explore more base conditions we try to move few indexes forward
# dp[1] to reach 1 we can only jump from index 0 which is 1 * dp[0]
# dp[2] to reach 2 we can jump from 0 or 1 which is 1* dp[0] + 1 * dp[1]
# dp[3] to reach step 3 we can jump from 1 or 2 
# dp[n] to reach step 4 we can jump from n-2 or n-1

# so our base conditions are dp[0] and dp[1] an recurring conditions are dp[n-1] and dp[n-2] starting from 2 to n:

# our solution is at dp[n]


##3 write recurring condition
#no ways = 1 * from (i-1) + 1* from (i-2) => 2 ways  
# no of distinct ways = 1 * no of distinct ways to reach (i-1) + 1 * no of distinct ways  to reach (i-2) 
# dp[i] = 1 * dp[i-1] + 1 *  dp[i-2]


## write the final solution

#
#
#
        #recursion
        # if n==0:
        #     return 1
        # if n ==1 : return 1
        # osways = self.climbStairs(n-1)
        # tsways = self.climbStairs(n-2)
        # return osways + tsways
        
        #dp
        dp = [0] * (n + 1)
        dp [0] ,dp[1] = 1,1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1] 