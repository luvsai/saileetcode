# Last updated: 18/12/2025, 20:19:49
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        msl = 0
        csl = 0
        cle = float('-inf')
        numset = set(nums)
        for ele in numset:
            
            if ele - 1 in numset:
                continue
            csl = 0
            while ele in numset:
                csl += 1
                
                ele +=1
            msl = max(msl, csl)
        return msl
        # nums = sorted(nums) # which is o(nlogn)
        # max_seq_len = 0
        # curr_seq_len = 0
        # pre_seq_element = float('-inf')

        # for ele in nums:
        #     if ele == pre_seq_element:
        #         continue
        #     if ele - 1 == pre_seq_element :
        #         curr_seq_len += 1
                
        #     else:
        #         curr_seq_len = 1
        #     pre_seq_element = ele
        #     max_seq_len = max(max_seq_len, curr_seq_len)
                        
        # return max_seq_len
