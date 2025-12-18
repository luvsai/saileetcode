# Last updated: 18/12/2025, 20:16:44
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic = [(heights[_], names[_]) for _ in range(len(names))]
        dic = sorted(dic, key= lambda pair : -pair[0])
        sortedNames = [dic[_][1] for _ in range(len(names))]
        return sortedNames

        