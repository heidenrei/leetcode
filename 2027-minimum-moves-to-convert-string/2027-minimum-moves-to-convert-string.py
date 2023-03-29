class Solution:
    def minimumMoves(self, s: str) -> int:
        N = len(s)
        s = [x for x in s]
        ans = 0
        for i in range(N-2):
            if s[i] == 'X':
                s[i:i+3] = [0]*3
                ans += 1
        
        extra = 'X' in s
        
        return ans + extra