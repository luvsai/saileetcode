# Last updated: 08/01/2026, 19:57:44
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(start_num, aux):
            if len(aux) == k:
                res.append(aux[:])
            
            for el in range(start_num, n+1):
                aux.append(el)
                backtrack(el + 1, aux)
                aux.pop()
        backtrack(1,[])
        return res
