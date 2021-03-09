class Solution:
    def removePalindromeSub(self, s: str) -> int:
        N = len(s)
        if not N:
            return 0
        # is it a palindrome? if so ret 1
        # else ret 2
        if N & 1:
            l = r = N//2
            while r < N:
                if s[l] != s[r]:
                    return 2
                l -= 1
                r += 1
            if r == N:
                return 1
        else:
            l = r = N//2 - 1
            r += 1
            while r < N:
                print(l, r)
                if s[l] != s[r]:
                    return 2
                l -= 1
                r += 1
                
            if r == N:
                return 1