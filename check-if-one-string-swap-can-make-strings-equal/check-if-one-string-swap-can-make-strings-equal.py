class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        N = len(s1)
        cnt = 0
        idxs = []
        for i in range(N):
            if s1[i] != s2[i]:
                cnt += 1
                idxs.append(i)
                if cnt > 2:
                    return False
        
        if cnt == 2:
            return s1[idxs[0]] == s2[idxs[1]] and s1[idxs[1]] == s2[idxs[0]]
        if not cnt:
            return True
        
        return False