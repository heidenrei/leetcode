class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        d = defaultdict(int)
        dlist = []
        curr = 1
        for x in pattern:
            if x not in d:
                d[x] = curr
                curr += 1
            dlist.append(d[x])
                
        d2 = defaultdict(int)
        dlist2 = []
        curr = 1
        for x in s:
            if x not in d2:
                d2[x] = curr
                curr += 1
            dlist2.append(d2[x])
            
        return dlist == dlist2
                
            