# Last updated: 18/12/2025, 20:18:33
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l1, l2 = len(p) , len(s)
        if l1> l2:
            return []

        p_count = Counter(p)
        window_counter = Counter(s[:l1])
        ans = []
        if p_count == window_counter:
            ans.append(0)
        for i in range(l1,l2):
            window_counter[s[i]] +=1
            window_counter[s[i-l1]] -=1
            if window_counter[s[i-l1] ] == 0:
                del window_counter[s[i-l1]]
            if p_count == window_counter:
                ans.append(i-l1 + 1)
        return ans