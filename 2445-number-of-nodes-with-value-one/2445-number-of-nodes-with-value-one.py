class Solution:
    def numberOfNodes(self, n: int, queries: List[int]) -> int:
        c = Counter(queries)
        ans = 0
        for x in range(1, n+1):
            tx = x
            cnt = 0
            while tx > 0:
                cnt += c[tx]
                tx >>= 1
            if cnt & 1:
                ans += 1
                
        return ans