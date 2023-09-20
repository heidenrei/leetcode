class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 0
        n = len(nums)
        pfs = 0
        ans = inf
        for i, x in enumerate(nums[::-1]):
            pfs += x
            if pfs == k:
                ans = i+1
            d[pfs] = i+1
        pfs = 0
        for i, x in enumerate(nums):
            pfs += x
            if k - pfs in d and (i+1) + d[k - pfs] <= n and ans > d[k - pfs] + (i+1):
                ans = (i+1) + d[k - pfs]
        return ans if ans < inf else -1