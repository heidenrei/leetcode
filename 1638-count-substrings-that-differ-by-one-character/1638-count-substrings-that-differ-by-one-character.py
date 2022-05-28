class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        ans = 0
        N = len(s)
        M = len(t)
        alpha = set([x for x in t])
        seen = set()
        for j in range(1, N+1): # 100
            for i in range(j): # 100
                ts = s[i:j]
                for k in range(M-(len(ts))+1):
                    tt = t[k:k+len(ts)]
                    has_d = False
                    good = True
                    for w in range(len(tt)):
                        if ts[w] != tt[w]:
                            if has_d:
                                good = False
                                break
                            else:
                                has_d = True
                    if has_d and good:
                        ans += 1
                            
        return ans
                