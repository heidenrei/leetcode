class Solution:
    def maxA(self, n: int) -> int:
        @cache
        def go(x, rem):
            if 0 <= rem <= 3:
                return rem
            if rem < 0:
                return -inf
            return max(go(x*3, rem-4)+x*2, go(x*4, rem-5)+x*3, go(x*2, rem-3)+x, go(x*5, rem-6)+4*x)
        return max(go(1, n-1)+1, go(2, n-2)+2, go(3, n-3)+3, go(4, n-4)+4)