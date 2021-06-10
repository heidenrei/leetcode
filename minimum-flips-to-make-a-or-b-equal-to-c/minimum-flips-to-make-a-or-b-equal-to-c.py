class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        bina = bin(a)[2:]
        binb = bin(b)[2:]
        binc = bin(c)[2:]
        
        maxl = len(max([bina, binb, binc], key=len))
        
        bina = bina.zfill(maxl)
        binb = binb.zfill(maxl)
        binc = binc.zfill(maxl)
        
        ans = 0
                
        for i in range(maxl):
            if binc[i] == '1':
                ans += all([bina[i] == '0', binb[i] == '0'])
            else:
                ans += sum([bina[i] == '1', binb[i] == '1'])
                
        return ans
            