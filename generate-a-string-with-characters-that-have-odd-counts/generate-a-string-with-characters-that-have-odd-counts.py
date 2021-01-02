class Solution:
    def generateTheString(self, n: int) -> str:
        return 'x' * n if n & 1 else 'x' * (n-1) + 'y'
