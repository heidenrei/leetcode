class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        N = len(s)
        to_remove = set()
        lefts = 0
        for i in range(N):
            if s[i] == '(':
                lefts += 1
            elif s[i] == ')':
                if lefts:
                    lefts -= 1
                else:
                    to_remove.add(i)
                    
        rights = 0
        for i in range(N)[::-1]:
            if s[i] == ')':
                rights += 1
            elif s[i] == '(':
                if rights:
                    rights -= 1
                else:
                    to_remove.add(i)
                    
        s = [x for i, x in enumerate(s) if i not in to_remove]
        
        return ''.join(s)