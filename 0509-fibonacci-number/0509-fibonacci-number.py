class Solution:
    def fib(self, n: int) -> int:
        if not n:
            return 0
        @cache
        def go(x):
            if x < 3:
                return 1
            return go(x-1) + go(x-2)
        return go(n)