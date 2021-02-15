class Solution:
    def fib(self, n: int) -> int:
        def go(num):
            if num == 1 or num == 2:
                return 1
            else:
                return go(num-1) + go(num-2)
            
        return go(n) if n != 0 else 0