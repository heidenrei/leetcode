class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        ans = 0
        d = defaultdict(int)
        for x in nums:
            ans |= x
            for i in range(32):
                if x & (1<<i):
                    d[i] += 1
        best = 0            
        for x in nums:
            tmp = ans
            for i in range(32):
                if x & (1<<i) and d[i] == 1:
                    tmp ^= 1<<i
            tmp |= (x<<k)
            
            if tmp > best:
                best = tmp
        return best