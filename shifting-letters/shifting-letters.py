class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        sfs = [shifts[-1]]
        for x in shifts[:-1][::-1]:
            sfs.append(x + sfs[-1])
        
        sfs.reverse()
        
        s = [x for x in s]
        for i in range(len(s)):
            s[i] = chr(ord('a') + (ord(s[i]) - ord('a') + sfs[i]) % 26)
            
        return ''.join(s)