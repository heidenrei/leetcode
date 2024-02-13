class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for x in words:
            n = len(x)
            if n & 1:
                if x[:n//2] == x[n//2+1:][::-1]:
                    return x
            else:
                if x[:n//2] == x[n//2:][::-1]:
                    return x
        return ''