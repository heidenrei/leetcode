class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        N = len(s)
        for i in range(N//2):
            if s[i] != s[N-i-1]:
                del_left = s[:i] + s[i+1:]
                del_right = s[:N-i-1] + s[N-i:]
                return del_left == del_left[::-1] or del_right == del_right[::-1]
            
        return False