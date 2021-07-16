class Solution:
    def shortestPalindrome(self, s: str) -> str:
        N = len(s)
        j = 1
        og = s
        while not s == s[::-1]:
            s = og[-j:][::-1] + og
            j += 1
            
        return s
