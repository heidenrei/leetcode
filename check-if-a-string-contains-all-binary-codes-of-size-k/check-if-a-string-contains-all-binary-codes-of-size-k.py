class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        N = len(s)
        
        c = ['1', '0']
        for i in range(k-1):
            tmp = []
            for el in c:
                tmp.append(el+'1')
                tmp.append(el+'0')
            c = tmp
        
        c = set(c)
        for i in range(N-k+1):
            tmp = s[i:i+k]
            if tmp in c:
                c.remove(tmp)
        return len(c) == 0