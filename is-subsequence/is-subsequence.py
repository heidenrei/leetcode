class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        s = deque([x for x in s])
        
        for i in range(len(t)):
            if t[i] == s[0]:
                s.popleft()
                if not s:
                    return True
                
        return False