# Last updated: 18/12/2025, 20:21:34
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_length = 0
        char_map =  {}
        for right, char in enumerate(s):
            if char in char_map and char_map[char] >= start:
                start = char_map[char] + 1
            char_map[char] = right
            max_length  = max( right - start + 1, max_length)
        return max_length