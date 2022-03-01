class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0 for x in range(n+1)]
        for x in range(n+1):
            ans[x] = x.bit_count()
            
        return ans