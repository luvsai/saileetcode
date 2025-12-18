# Last updated: 18/12/2025, 20:20:42
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        i = n-1
        carry = True
        while i>=0 :
            digit = digits[i]
            if carry:
                digit +=1
                carry = False
            ones = digit % 10
            digits[i] = ones
            if digit >= 10:
                carry = True
            i -=1
        if carry:
            digits.insert(0,1)
        return digits



        