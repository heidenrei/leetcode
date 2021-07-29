class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if len(a) != len(b):
            return len(max([a, b], key=len))
        
        a, b = sorted([a, b], key=len)
        N = len(a)
        
        for i in range(1, N+1)[::-1]:
            for j in range(N-i+1):
                if a[j:j+i] not in b:
                    return len(a[j:j+i])
                
        return -1
        