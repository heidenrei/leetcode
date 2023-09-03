class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f = lambda x: factorial(x)
        return f(n+m-2)//(f(m-1)*f(n-1))
    