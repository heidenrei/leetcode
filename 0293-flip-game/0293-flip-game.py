class Solution:
    def generatePossibleNextMoves(self, s):
        ans = []
        N = len(s)
        for i in range(N-1):
            if s[i:i+2] == '++':
                ans.append(s[:i] + '--' + s[i+2:])
                
        return ans