class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = '&' + s
        N = len(s)
        best = 1
        ans = s[1]
        for i in range(2, N):
            j = 1
            while 0 <= i - j and i + j < N and s[i-j] == s[i+j]:
                if j*2 + 1 > best:
                    ans = s[i-j:i+j+1]
                best = max(best, j*2 + 1)
                j += 1
                
            j = 0
            while 0 <= i - j - 1 and i + j < N and s[i-j-1] == s[i+j]:
                if j*2 + 2 > best:
                    ans = s[i-j-1:i+j+1]
                best = max(best, j*2 + 2)
                j += 1
            
        return ans
