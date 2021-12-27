class Solution:
    def findComplement(self, num: int) -> int:
        out = ''
        for i in range(len(bin(num)[2:])):
            out += str(1-int(bin(num)[2:][i]))
            
        return int(out, 2)