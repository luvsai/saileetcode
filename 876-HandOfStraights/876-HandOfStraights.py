# Last updated: 18/12/2025, 20:17:42
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize !=0:
            return False
        count = Counter(hand)

        for card in sorted (count):
            freq = count[card]
            if freq> 0:
                for i in range(groupSize):
                    if count[card+ i] < freq:
                        return False
                    count[card + i] -= freq
        return True