class Solution:
    def maxScore(self, s: str) -> int:
        N = len(s)
        
        zeros = []
        
        if s[0] == '0':
            zeros.append(1)
        else:
            zeros.append(0)
            
        for i in range(1, N):
            if s[i] == '0':
                zeros.append(zeros[-1]+1)
            else:
                zeros.append(zeros[-1])
                
        ones = []
        
        if s[-1] == '1':
            ones.append(1)
        else:
            ones.append(0)
            
        for i in range(N-2, -1, -1):
            if s[i] == '1':
                ones.append(ones[-1]+1)
            else:
                ones.append(ones[-1])
        
        ones.reverse()

        best = 0
        for i in range(1, N):
            best = max(best, zeros[i-1] + ones[i])

            
        return best