class Solution:
    def movesToStamp(self, s,t) -> List[int]:
        N = len(t)
        M = len(s)
        ans = []
        
        used = [0]*N
        s = list(s)
        old_t = t
        t = list(t)
        
        def go(offset):
            cnt = 0
            for i in range(M):
                if s[i] != t[i + offset] and t[i + offset] != '*':
                    return False
                if t[i + offset] != '*':
                    cnt += 1
                    
            return cnt > 0
        
        while True:
            found = 0
            
            for start in range(N-M+1):
                if go(start):
                    found = 1
                    for i in range(start, start+M):
                        t[i] = '*'
                    ans.append(start)
                    break
            if all(x == '*' for x in t):
                break
                
            if not found:
                return []
            
        ans.reverse()
        constructed = ['']*N
        for idx in ans:
            for k in range(M):
                constructed[idx + k] = s[k]
                
                
        if ''.join(constructed) == old_t:
            return ans
        
        return []