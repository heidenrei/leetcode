class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        d = defaultdict(int)
        for x, y in items:
            d[x] = max(d[x], y)
            
        keys = sorted([x for x in d])
        m = 0
        for x in keys:
            m = max(d[x], m)
            d[x] = m
        
        ans = []
        
        for q in queries:
            idx = bisect_right(keys, q)
            if idx == 0:
                ans.append(0)
            else:
                ans.append(d[keys[idx-1]])
                
        return ans
        