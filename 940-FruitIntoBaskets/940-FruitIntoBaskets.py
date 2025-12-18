# Last updated: 18/12/2025, 20:17:32
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)
        n = len(fruits)
        left = 0
        maxfruits = 0
        for right in range(n):
            basket[fruits[right]] +=1
            
            while len(basket) > 2:
                basket[fruits[left]] -=1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left +=1
            maxfruits = max(maxfruits, right - left +1)
        return maxfruits