# Last updated: 08/01/2026, 19:57:24
import string
from collections import deque

# “Since we want all shortest paths, we allow the same word to be reached multiple times within the same BFS level, but once a level is completed, we mark those words as visited so they are never used in deeper levels.”
import string

from collections import defaultdict, deque

from typing import List

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        # make a set of the word list for quick look up
        wordSet = set(wordList)
        
        # endWord not in wordList

        if endWord not in wordSet:
            return []
        parents = defaultdict(list)

        level = set()
        level.add(beginWord)
        found = False

        while level and not found :
            next_level = set()
            # for word in level:
            for word in level:
                wordSet.discard(word)

            
            # for every word in the level generate the transformation and make sure they are not present in word set
            for word in level:
                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        new_word = word[: i] + c + word[i+ 1:]
                        if new_word in wordSet:
                            next_level.add(new_word)
                            parents[new_word].append(word)
                            if new_word == endWord:
                                found = True
            level = next_level
        
        
        res = []
        def backtrack(word,path):
            if word == beginWord:
                res.append(path[::-1])
                return
            for p in parents[word]:
                backtrack(p, path + [p])
        if found :
            backtrack(endWord, [endWord])
        return res
		# #use dfs
		# wordSet = set(wordList)
		# visited = set(beginWord)
		# q = deque([([beginWord],1)])
		# flag = False
		# small_level = 0
		# finalarr = []
		# while q:
		# 	path, level = q.popleft()
		# 	word = path[-1]
			
		# 	if word == endWord:
		# 		if flag:
		# 			if level > small_level:
		# 				continue
		# 		finalarr.append(path)
		# 		small_level = level
		# 		flag = True
		# 	if flag :
		# 		continue
		# 	for i in range(len(word)):
		# 		for c in string.ascii_lowercase:
		# 			nword = word[:i] + c + word[i+1:]
		# 			# print(nword)
		# 			if nword in wordSet and nword not in path:
		# 				# visited.add(nword)
		# 				npath = path[:]
		# 				npath.append(nword)
		# 				q.append((npath,level +1))
		# return finalarr	