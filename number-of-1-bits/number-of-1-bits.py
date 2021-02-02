class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)[2:]
        N = len(n)
        cnt = 0
                
        for i in range(N):
            if n[i] == '1':
                cnt += 1
                
        return cnt