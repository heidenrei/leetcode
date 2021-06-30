class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t in s:
            return t
        
        i = 0
        j = 0
        best = math.inf
        best_ij = None
        
        ts = {x for x in t}
        tc = Counter(t)
        
        def is_possible():
            #print(s[i:j+1])
            possible = True
            for k in tc.keys():
                if tc[k] > 0:
                    possible = False
                    break
            if possible:
                nonlocal best
                if j - i < best:
                    nonlocal best_ij
                    best = j - i
                    best_ij = [i, j]
            return possible
        
        while j < len(s):
            if s[j] in ts:
                tc[s[j]] -= 1
                good = is_possible()
                #print(s[i:j+1], 'is good:', good, [i, j], tc)

                if good:
                    if s[i] in ts:
                        tc[s[i]] += 1
                        
                    i += 1
                    is_possible()

                    while 1:
                        if not i < len(s):
                            break
                        if s[i] not in ts:
                            i += 1
                        elif s[i] in ts and tc[s[i]] < 0:
                            tc[s[i]] += 1
                            is_possible()
                            i += 1
                        else:
                            is_possible()
                            break
                        
                    
                        
            
            j += 1
            
        j -= 1
        is_possible()
        
        return s[best_ij[0]:best_ij[1]+1] if best_ij else ''