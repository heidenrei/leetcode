class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        
        gi = 0
        si = 0
        
        ans = 0
        
        while si < len(s):
            if s[si] >= g[gi]:
                gi += 1
                si += 1
                ans += 1
            else:
                gi += 1
            
            if gi == len(g):
                break
                
        return ans