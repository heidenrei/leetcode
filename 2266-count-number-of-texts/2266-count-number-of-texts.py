class Solution:
    def countTexts(self, s: str) -> int:
        MOD = 10**9+7
        N = len(s)
        @cache
        def go(i):
            if i == N:
                return 1
            ans = 0
            if s[i] in '79':
                for j in range(4):
                    if i+j == N or s[i] != s[i+j]:
                        break
                    else:
                        ans += go(i+j+1)
                        ans %= MOD
            else:
                for j in range(3):
                    if i+j == N or s[i] != s[i+j]:
                        break
                    else:
                        ans += go(i+j+1)
                        ans %= MOD
                        
            return ans
        
        return go(0)