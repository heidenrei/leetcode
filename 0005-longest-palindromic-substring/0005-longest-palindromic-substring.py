class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        ans = 1
        out = s[0]
        for i in range(N):
            di = 0
            while i + di < N and i - di >= 0 and s[i+di] == s[i-di]:
                di += 1
            di -= 1
            if di > 0:
                tmp = di * 2 + 1
                if tmp > ans:
                    ans = tmp
                    out = s[i-di:i+di+1]
            if i + 1 < N and s[i] == s[i+1]:
                if 2 > ans:
                    ans = 0
                    out = s[i:i+2]
                di = 0
                while i + di + 1 < N and i - di >= 0 and s[i+di+1] == s[i-di]:
                    di += 1
                di -= 1
                if di > 0:
                    tmp = di * 2 + 2
                    if tmp > ans:
                        ans = tmp
                        out = s[i-di:i+di+2]
        print(ans)  
        return out