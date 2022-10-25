class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = defaultdict(list)
        for x in nums:
            ds = sum([int(y) for y in str(x)])
            d[ds].append(x)
            
            
        best = -1
        for k in d:
            d[k].sort()
            if len(d[k]) > 1:
                best = max(best, sum(d[k][-2:]))
        
        return best