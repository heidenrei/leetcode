class Solution:
    def countVowelStrings(self, n: int) -> int:
        @cache
        def go(i, rem):
            if rem == 0:
                return 1
            ans = 0
            for j in range(i, 5):
                ans += go(j, rem-1)
            return ans
        
        return go(0, n)