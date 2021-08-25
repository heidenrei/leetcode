class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for x in range(math.floor(math.sqrt(c)+1)):
            if (c - x**2)**0.5 % 1 == 0:
                return True
            
        return False