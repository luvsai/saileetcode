# Last updated: 18/12/2025, 20:17:26
class Solution:
    memory = []
    def fibr(self, n: int , flag) -> int:            
        #print("call for  n :", n )
        if self.memory[n] == -1:
            self.memory[n ] = self.fibr(n - 1, 1) + self.fibr(n - 2, 1) 
        return self.memory[n]
    def fib(self, n: int) -> int:
        if n == 1 :
            return 1
        if n == 0 : 
            return 0
        self.memory = [-1] * (n + 1) 
        self.memory[0] = 0
        self.memory[1] = 1
        #print( "Initial : " , self.memory)
        self.fibr(n, 0)
        # print("Final : ", self.memory)
        # print(self.memory[n])
        return self.memory[n]
        



        
