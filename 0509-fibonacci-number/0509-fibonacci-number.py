class Solution:
    def fib(self, n: int) -> int:
        if not n:
            return 0
        
        def go(n):
            if n < 3:
                return 1
            return go(n-1) + go(n-2)
        return go(n)