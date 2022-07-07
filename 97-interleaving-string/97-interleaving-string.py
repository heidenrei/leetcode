class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        N1 = len(s1)
        N2 = len(s2)
        N3 = len(s3)
        
        if not all([s1, s2, s3]):
            return s1 + s2 == s3
        
        if N1+N2 != N3:
            return False
        
        p1 = 0
        p2 = 0
        
        @cache
        def go(p1, p2):
            if p1 + p2 == N3:
                return True
            
            one, two = False, False
            
            if p1 < N1 and s3[p1+p2] == s1[p1] and go(p1+1, p2):
                return True
            
            if p2 < N2 and s3[p1+p2] == s2[p2] and go(p1, p2+1):
                return True
            
            return False
            
        return go(0, 0) if any([s1, s2, s3]) else True