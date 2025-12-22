# Last updated: 22/12/2025, 19:26:31
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        even_positions = (n + 1) // 2
        odd_positions = n // 2

        return (pow(5, even_positions, MOD) * 
                pow(4, odd_positions, MOD)) % MOD
