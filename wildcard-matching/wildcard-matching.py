class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if '*' in p and len(set(p)) == 1:
            return True

        if '*' in p and '?' in p and len(set(p)) == 2:
            if p.count('?') <= len(s):
                return True
            else:
                return False
        
        tmp = ''
        
        for i in range(len(p)):
            if p[i] == '*':
                if not tmp or tmp[-1] != '*':
                    tmp += '*'
            else:
                tmp += p[i]
                
        p = tmp
        
        sn = len(s)
        pn = len(p)
        
        d = defaultdict(list)
        
        for i in range(sn):
            d[s[i]].append(i)
        
        found_ans = False
        
        @cache
        def go(i, j):
            
            print(s[i:], p[j:])
            
            while i < sn and j < pn and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
                if i == sn or j == pn:
                    break
            if i == sn and j == pn or (j == pn - 1 and p[j] == '*'):
                nonlocal found_ans
                found_ans = True
                return
                
            if j < pn and p[j] == '*':
                if p[j+1] == '?':
                    for k in range(sn-i):
                        go(i+k, j+1)
                for idx in d[p[j+1]]:
                    if idx >= i:
                        go(idx, j+1)
                        
        go(0, 0)
        
        return found_ans