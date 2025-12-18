# Last updated: 18/12/2025, 20:19:51
from collections import deque
import string
# from collection import deque
import string

#Time Complexity=O(N×L×26) => O(N×L)
#space Space Complexity=O(N×L) 
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
        wordSet = set(wordList)
        bfsQ = deque([(beginWord, 1)])
        visited = set(beginWord)
        alpha = string.ascii_lowercase
        while bfsQ:
            word, level = bfsQ.popleft()
            if word == endWord:
                return level
            for i in range(len(word)):
                for c in alpha:
                    nword = word[:i] + c  + word[i +1 : ]
                    if nword in wordSet and nword not in visited:
                        bfsQ.append((nword,level  + 1))
                        visited.add(nword)
        return 0
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
        #  create a set of wordList
        wordSet = set(wordList)
        bfsQ = deque([(beginWord, 1)])
        visited = set(beginWord)
        alpha = string.ascii_lowercase
        while bfsQ :
            word , level = bfsQ.popleft()
            if word == endWord:
                return level
            for i in range(len(word)):
                for c in alpha:
                    nword = word[:i] + c + word[i+1 :]
                    if nword in wordSet and nword not in visited:
                        bfsQ.append((nword, level + 1))
                        visited.add(nword)
        return 0


# Time Complexity

# Let:

# \U0001d43f
# L = length of each word

# \U0001d441
# N = number of words in wordList

# Step-by-step:

# For each word popped from the queue, you:

# Loop through L positions in the word.

# For each position, try replacing it with 26 letters ('a' to 'z').

# → So for each word, you can generate 26 × L possible transformations.

# Checking membership (if nword in wordSet) is O(1) average time since wordSet is a hash set.

# Each valid word (node) is added to the queue at most once, because of the visited set.

# ✅ Therefore:

# Time Complexity
# =
# \U0001d442
# (
# \U0001d441
# ×
# \U0001d43f
# ×
# 26
# )
# Time Complexity=O(N×L×26)

# → Simplifies to:

# \U0001d442
# (
# \U0001d441
# ×
# \U0001d43f
# )
# O(N×L)

# (since 26 is a constant factor)

# \U0001f9e0 Space Complexity

# wordSet → stores all words → O(N)

# visited → at most all words visited → O(N)

# bfsQ → at most all words in queue → O(N)

# Temporary strings (nword) generated during loops → O(L)

# ✅ Therefore:

# Space Complexity
# =
# \U0001d442
# (
# \U0001d441
# ×
# \U0001d43f
# )
# Space Complexity=O(N×L)

# (because you store up to N words, each of length L)