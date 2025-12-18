# Last updated: 18/12/2025, 20:18:15
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

#Use Sliding Window and Frequency Count:

# The core idea is to use a sliding window over s2 that is the same length as s1.
# Compare the frequency of characters in the current window of s2 with the frequency of characters in s1.
# If they match, it means a permutation of s1 is a substring in s2.

        l1, l2 = len(s1), len(s2)
        if l1> l2 :
            return False
            
        
        s1_counter = Counter(s1)
        
        window_counter = Counter(s2[:l1])
        
        if s1_counter == window_counter :
            return True

        for i in range(l1, l2):
            window_counter[s2[i]] +=1
            window_counter[s2[i - l1]] -=1
            if window_counter[s2[i-l1]] == 0:
                del window_counter[s2[i-l1]]

            if s1_counter == window_counter :
                return True    
        return False