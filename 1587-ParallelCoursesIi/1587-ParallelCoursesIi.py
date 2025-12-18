# Last updated: 18/12/2025, 20:17:07
class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        #dp[mask] = min semesters to finish all the courses in mask

        # we would need prequisites as bitmasks
        # for each course i (0 indexed)
        # pr[i] = bimask of courses that must be done before i

        # all prerequisites done check:
        # pr[i] & mask == pr[i]

        # S2 for given mask , determine the available courses
        # A course is available if
            # It is not already taken (mask >> i) & 1 == 0
            # all prerequisites are done (pr[i] & mask ) == pre[i]
        #we OR all such courses into avail_mask
        # which represents all the courses that we could take. right now.

        #s3 picking subsets of available courses of lenght <=k

        # s4 dp transition
        #new_mask = mask | sub
        # dp[new_mask] = min(dp[new_mask], dp[mask] + 1)
        # mask -> previous set of finished courses
        # sub -> courses you take this semester
        # new_mask -> what you'll have completed next semester
        # + 1 -> because one semester passes
        # this is standard dfs relaxation.

        # step 5 optimization :
        # if available courses <= k take all courses.
        
        # avail_mask.bitcount() <=k :
        # there is no reason to consider subsets
        # new_mask = mask |avail
        # dp[new_mask] = dp[mask] + 1
        # # this reduces branching masively
        # step6 enumerate subsets efficiently
        # sub = avail_mask
        # while sub> 0:
        #     consider sub
        #     sub = (sub -1 )  & avail_mask
        prereq = [0] * n
        for u, v in relations:
            prereq[v-1] |= 1 << (u-1)
        FULL = (1<<n) -1

        # 
        dp = [float('inf')] * (1<<n)
        dp[0] = 0 
        for mask in range( 1<<n):
            if dp[mask] == float('inf'):
                continue
            #find the available courses
            avail_mask = 0
            for c in range(n):
                if not (mask & (1 << c)) and (prereq[c] & mask) == prereq[c]:
                    avail_mask |= (1<< c)
            # if no available courses , continue
            if avail_mask == 0:
                continue

            # count how manyu avaible
            cnt = avail_mask.bit_count()
            
            # if cnt is <= k take all availble courses and move to next mask
            if cnt <= k :
                new_mask = mask | avail_mask
                dp[new_mask] = min(1 + dp[mask], dp[new_mask])
                continue

            # else enumerate subsets up to k

            sub = avail_mask
            while sub:
                if sub.bit_count() <=k:
                    new_mask = mask | sub
                    dp[new_mask] = min(dp[new_mask], dp[mask] + 1)
                sub = (sub -1 ) & avail_mask
        return dp[FULL]
        


