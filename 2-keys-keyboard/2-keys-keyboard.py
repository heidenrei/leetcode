class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        @cache
        def go(x, c):
            if x == n:
                return 0
            
            if x + c <= n:
                return min(go(x+c, c) + 1, go(x+c, x+c) + 2)
            else:
                return math.inf
            
        return go(1, 1)  + 1