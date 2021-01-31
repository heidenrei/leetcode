class Solution:
    def countBalls(self, l: int, h: int) -> int:
        d = defaultdict(int)
        
        for i in range(l, h+1):
            tmp = str(i)
            tmp = [int(x) for x in tmp]
            d[sum(tmp)] += 1
            
        ans = 0
            
        for k, v in d.items():
            ans = max(ans, v)
            
        return ans