class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bx = bin(x)[2:]
        by = bin(y)[2:]
        
        N = len(max(bx, by, key=len))
        bx = bx.zfill(N)
        by = by.zfill(N)
                
        ans = 0
        for i in range(N):
            if bx[i] != by[i]:
                ans += 1
        return ans