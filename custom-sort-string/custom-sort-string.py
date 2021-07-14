class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = defaultdict(int)
        cnt = 1
        for ch in order:
            d[ch] = cnt
            cnt += 1
        
        extras = ''
        tmp = []
        for x in s:
            if x in d:
                tmp.append(x)
            else:
                extras += x
                
        tmp.sort(key=lambda x: d[x])
        
        return ''.join(tmp) + extras