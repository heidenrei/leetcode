class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        
        l = 0
        r = len(s) - 1
        
        skipped = False
        rr = True
        rl = True
        while l < r:
            if s[l] != s[r]:
                if not skipped:
                    skipped = True
                    r -= 1
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                rr = False
                break
            
        s = s[::-1]
        
        l = 0
        r = len(s) - 1
        
        skipped = False
        while l < r:
            if s[l] != s[r]:
                if not skipped:
                    skipped = True
                    r -= 1
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                rl = False
                break
            
        return rl or rr