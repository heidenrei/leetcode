class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded)+1
        x = 0
        
        # gets xor of all the numbers in the permutation
        for i in range(1,n+1):
            x^=i
            
        # xors every second el in encoded with x...
        for i in range(1, n-1, 2):
            x ^= encoded[i]
            
        res = [0]*n
        res[0] = x
        
        for i,e in enumerate(encoded):
            res[i+1]=res[i]^e
            
        return res
            
