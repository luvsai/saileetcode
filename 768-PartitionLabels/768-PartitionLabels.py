# Last updated: 18/12/2025, 20:17:56
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ch_dict = {ch :i for i, ch in enumerate(s)}
        res = []
        start = end = 0
        for i, ch in enumerate(s):
            end = max(end, ch_dict[ch])
            if i == end:
                res.append(end-start +1)
                start = i +1
        return res
        