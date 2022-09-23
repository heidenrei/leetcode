class Solution:
    def concatenatedBinary(self, n: int) -> int:
        bini = ''
        
        for i in range(1, n+1):
            bini += bin(i)[2:]
            
        return int(bini, 2) % (10**9+7)