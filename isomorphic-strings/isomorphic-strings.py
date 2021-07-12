class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        def transcode(x):
            cnt = 1
            d = defaultdict(int)
            s_code = []
            for ch in x:
                if ch in d:
                    s_code.append(d[ch])
                else:
                    cnt += 1
                    d[ch] = cnt
                    s_code.append(cnt)
                    
            return s_code
        
        return transcode(s) == transcode(t)