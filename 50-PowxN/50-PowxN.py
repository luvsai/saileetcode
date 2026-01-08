# Last updated: 08/01/2026, 19:57:56
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n ==0 :
            return 1.0
        if n < 0:
            x = 1/x
            n = -n
        count  = 0
        def fastPow(x, n):
            global count
    
            # base 
            if n == 0:
                return 1
            half = fastPow(x, n//2)
            if n% 2 == 0:
                return half * half
                count +=1
            else:
                return x * half * half
                count +=2
        
        ans = fastPow(x,n)
        # print(count)
        return ans


            
        