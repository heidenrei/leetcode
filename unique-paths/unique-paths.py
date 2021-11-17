class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m*n == 0:
            return 0
        return factorial(m+n-2)//(factorial(m-1)*factorial(n-1))