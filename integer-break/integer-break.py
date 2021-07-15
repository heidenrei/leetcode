class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 5:
            return [0, 0, 1, 2, 4][n]
        
        if divmod(n, 3)[1] == 0:
            return 3**(n//3)
        if divmod(n, 3)[1] == 2:
            return 3**(n//3)*2
        
        return 3**(n//3-1)*4