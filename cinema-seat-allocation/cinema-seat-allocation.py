class Solution:
    def maxNumberOfFamilies(self, n: int, res: List[List[int]]) -> int:
        d = defaultdict(set)
        for x, y in res:
            if 1 < y < 10:
                d[x].add(y)
            
        ans = (n - len(d.keys())) * 2
        
        left = set([2,3,4,5])
        mid = set([4,5,6,7])
        right = set([6,7,8,9])
                
        for k, v in d.items():
            nv = len(v) + 4
            l = len(left ^ v) == nv
            m = len(mid ^ v) == nv
            r = len(right ^ v) == nv
                        
            ans += max([m, l+r])
            
        return ans