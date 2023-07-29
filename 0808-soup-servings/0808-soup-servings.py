class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1
        @cache
        def go(a, b):
            if a >= n and b >= n:
                return 0.5
            if a >= n:
                return 1
            if b >= n:
                return 0
            return go(a+100, b)*0.25 + go(a+75, b+25)*0.25 + go(a+50, b+50)*0.25 + go(a+25, b+75)*0.25
        ans = go(0, 0)
        ans = round(ans, 5)
        return ans